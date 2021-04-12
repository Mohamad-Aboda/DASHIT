from flask import Flask, render_template, send_from_directory, abort, redirect, url_for, session, logging, request, jsonify, flash, send_file
from random import sample
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from functools import wraps
from werkzeug.utils import secure_filename
import KPIs, charts
import GeneralKPIs, GeneralCharts
import Filtering
import json
import os
import re
import generator
import generalGenerator
import deleteDashboard
import FinancialKPIs, FinancialCharts
from distutils.dir_util import copy_tree
import pandas as pd
import pickle
import io
import csv
from flask import Flask, render_template
import sys
import logging


app = Flask(__name__)



app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
emailRegex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# application config
app.config['MYSQL_HOST'] = 'us-cdbr-east-03.cleardb.com'
app.config['MYSQL_USER'] = 'b30c1f9a1cf586'
app.config['MYSQL_PASSWORD'] = 'fc0ff0bf'
app.config['MYSQL_DB'] = 'heroku_dd81ad0ab4592be'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = 'CSV'

mysql = MySQL(app)


# checks if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/signin')
    return wrap


# homepage
@app.route('/')
def home():
    return render_template('home.html')

# dashboard
@app.route('/dashboard')
@is_logged_in
def dashboardSelector():
    return render_template(session['username'] + '/dashboardselector.html')

@app.route('/dashboard/<dashboard>')
@is_logged_in
def dashboard(dashboard):
    return render_template(session['username']+ '/' + dashboard +'.html')

@app.route('/dashboard/generate')
@is_logged_in
def dashboardGenerator():
    return render_template('dashboardgenerator.html')

# registration sql class


class RegisterForm(Form):
    username = StringField('Username', [validators.Length(
        min=4, max=25)])
    email = StringField('Name', [validators.Length(
        min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired()
    ])
    confirm = PasswordField('Confirm Password')

def checkEmail(email):
    if(re.search(emailRegex, email)):
        return True
    else:
        return False

# sign up page and fetch the data from the page to insert it in sql
@app.route('/signup', methods=['GET', 'Post'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        cur = mysql.connection.cursor()
        username = form.username.data
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        if result > 0:
            flash("Username already exists")
            cur.close()
            return redirect('/signup')
        else:
            email = form.email.data
            if(checkEmail(email) == False):
                flash("Enter a valid Email")
                cur.close()
                return redirect('/signup')
            result = cur.execute("SELECT * FROM users WHERE email = %s", [email])
            if result > 0:
                flash("Email already exists")
                cur.close()
                return redirect('/signup')
            else:
                if(str(form.password.data) == str(form.confirm.data)):
                    password = sha256_crypt.hash(str(form.password.data))
                    cur.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s)",
                                (username, email, password))
                    flash('Success-Registration completed successfully')
                    mysql.connection.commit()
                    os.mkdir('CSV\\' + username)
                    os.mkdir('templates\\' + username)
                    with open('CSV\\' + username + '\\' + 'template.csv', 'w') as fc:
                        fc.write('TV,Radio,Social Media,Influencer')
                        fc.close()
                    copy_tree('templates/Base', 'templates/' + username)
                    return redirect('/signin')
                else:
                    flash('Passwords do not match')
                    cur.close()
                    return redirect('/signup')
        cur.close()
    return render_template('signup.html', form=form)


# sign in and handle the checking
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        if(result == 0 and username != ''):
            flash('Incorrect Username or Password')
        elif result > 0:
            data = cur.fetchone()
            password = data['password']
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username
                return redirect('/')
                cur.close()
            else:
                flash('Incorrect Username or Password')
    return render_template('signin.html')


# loggin out by clearing the session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/filter/pos/<location>', methods=['POST'])
@is_logged_in
def posFilter(location):
    location = session['username'] + '/' + location
    rf = request.form
    for key in rf.keys():
        data = key
    data_dic = json.loads(data)
    brand = data_dic['Brand']
    city = data_dic['City']
    product = data_dic['Product']
    store = data_dic['Store']
    country = data_dic['Country']
    startdate = "-".join(data_dic['StartDate'].split('-')[::-1])
    if startdate == '':
        startdate = 'All'
    enddate = "-".join(data_dic['EndDate'].split('-')[::-1])
    if enddate == '':
        enddate = 'All'
    filteredData = Filtering.applyFilters(location, startdate, enddate, country, city, store, brand, product)
    return jsonify({'totalSales': KPIs.total_sales(filteredData, 1),
                    'salesPerStore': KPIs.sales_per_store(filteredData, 1),
                    'totalOnhandAmount': KPIs.total_onhand_amount(filteredData, 1),
                    'totalOnhandUnits': KPIs.total_onhand_units(filteredData, 1),
                    'averageInventoryAmount': KPIs.average_inventory_amount(filteredData, 1),
                    'distinctProductsSold': KPIs.ditinct_products_sold(filteredData, 1),
                    'outOfStock': KPIs.out_of_stock(filteredData, 1),
                    'totalsalesPerDay': json.loads(charts.totalsales_per_day(location)),
                    'totalsalesPerCountry': json.loads(charts.totalsales_per_country(location)),
                    'topProducts': json.loads(charts.top_products(location)),
                    'topBrands': json.loads(charts.top_brands(location)),
                    'totalsalesPerCity': json.loads(charts.totalsales_per_city(location)),
                    'totalsalesPerStore': json.loads(charts.totalsales_per_store(location)),
                    'salesPercentageForBrand': json.loads(charts.sales_percentage_for_brand(location))
                    })


# api for the data
@app.route('/data/pos/<location>')
@is_logged_in
def posData(location):
    location = session['username'] + '/' + location
    return jsonify({'totalSales': KPIs.total_sales(location),
                    'salesPerStore': KPIs.sales_per_store(location),
                    'totalOnhandAmount': KPIs.total_onhand_amount(location),
                    'totalOnhandUnits': KPIs.total_onhand_units(location),
                    'averageInventoryAmount': KPIs.average_inventory_amount(location),
                    'distinctProductsSold': KPIs.ditinct_products_sold(location),
                    'outOfStock': KPIs.out_of_stock(location),
                    'totalsalesPerDay': json.loads(charts.totalsales_per_day(location)),
                    'totalsalesPerCountry': json.loads(charts.totalsales_per_country(location)),
                    'topProducts': json.loads(charts.top_products(location)),
                    'topBrands': json.loads(charts.top_brands(location)),
                    'totalsalesPerCity': json.loads(charts.totalsales_per_city(location)),
                    'totalsalesPerStore': json.loads(charts.totalsales_per_store(location)),
                    'salesPercentageForBrand': json.loads(charts.sales_percentage_for_brand(location))
                    })

@app.route('/data/general/<location>')
@is_logged_in
def generalData(location):
    location = session['username'] + '/' + location
    f = open('templates/' + location + '.json')
    data = json.load(f)
    kpiData = {}
    chartData = {}
    jsonData = {}
    f.close
    for k in data['kpi']:
        kpiData[k] = str(GeneralKPIs.create_KPI(location, data['kpi'][k]['columns'], data['kpi'][k]['operation']))
    for chart in data['chart']:
        print(location)
        chartData[chart] = json.loads(GeneralCharts.create_chart(location, data['chart'][chart]['columns'], data['chart'][chart]['type']))
        chartData[chart]['type'] =  data['chart'][chart]['type']
    jsonData['kpi'] = kpiData
    jsonData['chart'] = chartData
    return jsonData


@app.route('/filter/finance', methods=['POST'])
@is_logged_in
def financeFilter():
    rf = request.form
    for key in rf.keys():
        data = key
    data_dic = json.loads(data)
    brand = data_dic['Brand']
    city = data_dic['City']
    product = data_dic['Product']
    store = data_dic['Store']
    country = data_dic['Country']
    startdate = "-".join(data_dic['StartDate'].split('-')[::-1])
    if startdate == '':
        startdate = 'All'
    enddate = "-".join(data_dic['EndDate'].split('-')[::-1])
    if enddate == '':
        enddate = 'All'
    filteredData = Filtering.applyFilters(
        'pos', startdate, enddate, country, city, store, brand, product)
    return jsonify({'totalSales': str(KPIs.total_sales(filteredData, 1)),
                    'salesPerStore': str(KPIs.sales_per_store(filteredData, 1)),
                    'totalOnhandAmount': str(KPIs.total_onhand_amount(filteredData, 1)),
                    'totalOnhandUnits': str(KPIs.total_onhand_units(filteredData, 1)),
                    'averageInventoryAmount': str(KPIs.average_inventory_amount(filteredData, 1)),
                    'distinctProductsSold': str(KPIs.ditinct_products_sold(filteredData, 1)),
                    'outOfStock': str(KPIs.out_of_stock(filteredData, 1)),
                    'totalsalesPerDay': json.loads(charts.totalsales_per_day('pos')),
                    'totalsalesPerCountry': json.loads(charts.totalsales_per_country('pos')),
                    'topProducts': json.loads(charts.top_products('pos')),
                    'topBrands': json.loads(charts.top_brands('pos')),
                    'totalsalesPerCity': json.loads(charts.totalsales_per_city('pos')),
                    'totalsalesPerStore': json.loads(charts.totalsales_per_store('pos')),
                    'salesPercentageForBrand': json.loads(charts.sales_percentage_for_brand('pos'))
                    })


# api for the data
@app.route('/data/finance')
@is_logged_in
def financeData():
    return jsonify({'totalRevenue' : str(FinancialKPIs.total_revenues('finance')),
                    'COGS' : str(FinancialKPIs.COGS('finance')),
                    'opEX' : str(FinancialKPIs.OpEx('finance')),
                    'grossMargin' : str(FinancialKPIs.gross_margin('finance')),
                    'grossMarginPercentage' : str(FinancialKPIs.gross_margin_percentage('finance')),
                    'opExToRevenue' : str(FinancialKPIs.OpEx_to_revenue('finance')),
                    'deprecAndAmort' : str(FinancialKPIs.deprec_and_amort('finance')),
                    'operationIncome' : str(FinancialKPIs.operating_income('finance')),
                    'operatingIncomePercentage' : str(FinancialKPIs.operating_income_percentage('finance')),
                    'totalRevenuePerMonth' :  json.loads(FinancialCharts.total_revenue_per_month('finance')),
                    'totalRevenuePerCompany' : json.loads(FinancialCharts.total_revenue_per_company('finance')),
                    'COGSPerCompany' : json.loads(FinancialCharts.COGS_per_company('finance')),
                    'grossMarginPerCompany' : json.loads(FinancialCharts.gross_margin_per_company('finance')),
                    'grossMarginPercentagePerCompany' : json.loads(FinancialCharts.gross_margin_percentage_per_company('finance')),
                    'OPEXPerCompany' : json.loads(FinancialCharts.OPEX_per_company('finance')),
                    'OPEXToRevenuePerCompany' : json.loads(FinancialCharts.OPEX_to_revenue_per_company('finance'))
                    })


@app.route('/generate', methods=['POST'])
@is_logged_in
def generate():
    rf = request.form
    for key in rf.keys():
        data = key
    data_dic = json.loads(data)
    if(data_dic['type'] == 'General'):
        message = generalGenerator.generate(session['username'],data_dic['name'], data_dic['kpi'], data_dic['chart'])
    else:
        message = generator.generate(session['username'], data_dic['name'], data_dic['type'], data_dic['KPIs'])
    return jsonify({'Success': True})

@app.route('/delete', methods=['POST'])
@is_logged_in
def delete():
    rf = request.form
    for key in rf.keys():
        data = key
    data_dic = json.loads(data)
    deleteDashboard.remove(session['username'] ,data_dic['name'])
    return jsonify({'Success': 'True'})


# check extension of the uploaded file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# upload page
@app.route('/upload', methods=['GET', 'POST'])
@is_logged_in
def upload():
    if request.method == 'POST':
        # saves each file in the corresponding directory
        folder = request.form.get('upload').split('_')[1]
        if request.files:
            file = request.files[folder]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'] +  '/' +  session['username'] +'/' + folder +'/', filename))
                flash(folder.upper() + '-' +file.filename + ' uploaded successfully')
        return redirect(request.url)
    return render_template(session['username'] + '/upload.html')

@app.route('/predict', methods=['GET', 'POST'])
@is_logged_in
def predict():
    if request.method == 'POST':
        # saves each file in the corresponding directory
        folder = request.form.get('upload').split('_')[1]
        if request.files:
            file = request.files[folder]
            if file and allowed_file(file.filename):
                data = pd.read_csv(file)
                model = pickle.load(open('marketModel.pkl', 'rb'))
                p = model.predict(data)
                row = p
                proxy = io.StringIO()
                
                writer = csv.writer(proxy)
                writer.writerow(row)
                
                # Creating the byteIO object from the StringIO Object
                mem = io.BytesIO()
                mem.write(proxy.getvalue().encode())
                # seeking was necessary. Python 3.5.2, Flask 0.12.2
                mem.seek(0)
                proxy.close()

                return send_file(
                    mem,
                    as_attachment=True,
                    attachment_filename='output.csv',
                    mimetype='text/csv'
                )
    return render_template(session['username'] + '/predict.html')

@app.route('/download/<path:p>')
@is_logged_in
def downloadFile(p):
    print('CSV/' + session['username'] + '/' + p.split('template')[0])
    return send_from_directory('CSV/' + session['username'] + '/' + p.split('template')[0], filename=p.split('/')[-1], as_attachment=True)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
