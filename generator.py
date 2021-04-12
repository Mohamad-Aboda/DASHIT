import os

def totalSales():
    return '<div class="halfcard">\n  <div class="averageSales">\n    <div class="halfcardcontent">\n      <div class="count_content">\n        <h6>Total Sales</h6>\n        <h2><span class="counter" id="totalSales"></span> EGP</h2>\n      </div>\n    </div>\n  </div>\n</div>\n'

def averageInventoryAmount():
    return '<div class="halfcard">\n  <div class="averageSales">\n    <div class="halfcardcontent">\n      <div class="count_content">\n        <h6>Average Inventory Amount</h6>\n        <h2><span class="counter" id="averageInventoryAmount"></span>EGP</h2>\n      </div>\n    </div>\n  </div>\n</div>\n'

def totalOnhandAmount():
    return '<div class="halfcard">\n  <div class="averageSales">\n    <div class="halfcardcontent">\n      <div class="count_content">\n        <h6>Total OnHand Amount</h6>\n        <h2><span class="counter" id="totalOnhandAmount"></span>EGP</h2>\n      </div>\n    </div>\n  </div>\n</div>\n'

def salesPerStore():
    return '<div class="halfcard">\n  <div class="averageSales">\n    <div class="halfcardcontent">\n      <div class="count_content">\n        <h6>Sales Per Store</h6>\n        <h2><span class="counter" id="salesPerStore"></span>EGP</h2>\n      </div>\n    </div>\n  </div>\n</div>\n'

def distinctProductsSold():
    return '<div class="halfcard">\n  <div class="averageSales">\n    <div class="halfcardcontent">\n      <div class="count_content">\n        <h6>Distinct Products Sold</h6>\n        <h2><span class="counter" id="distinctProductsSold"></span></h2>\n      </div>\n    </div>\n  </div>\n</div>\n'

def outOfStock():
    return '<div class="halfcard">\n  <div class="averageSales">\n    <div class="halfcardcontent">\n      <div class="count_content">\n        <h6>Out Of Stock</h6>\n        <h2><span class="counter" id="outOfStock"></span></h2>\n      </div>\n    </div>\n  </div>\n</div>\n'

def totalSalesPerDay():
    return '<div class="card">\n    <div class="chart" id="totalsalesperday"></div>\n</div>\n'

def totalSalesPerCountry():
    return '<div class="card">\n    <div class="chart" id="totalsalespercountry"></div>\n</div>\n'

def totalSalesPerCity():
    return '<div class="card">\n    <div class="chart" id="totalsalespercity"></div>\n</div>\n'

def totalSalesPerStore():
    return '<div class="card">\n    <div class="chart" id="totalsalesperstore"></div>\n</div>\n'

def topProducts():
    return '<div class="card">\n    <div class="chart" id="topproducts"></div>\n</div>\n'

def topBrands():
    return '<div class="card">\n    <div class="chart" id="topbrands"></div>\n</div>\n'

def salesPercentageForBrand():
    return '<div class="doubleCard"> <div class="chart" id="salespercentageforbrand"></div></div>'

def createFile(username ,name, dashboardType, KPIs):
    f = open('templates/' + username + '\\' + name + '.html', "w")
    f.write('<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8" />\n    <meta http-equiv="X-UA-Compatible" content="IE=edge" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n    <link\n      rel="stylesheet"\n      type="text/css"\n      href="{{ url_for("static", filename="navstyle.css") }}"\n    />\n    <script\n      src="https://kit.fontawesome.com/64d58efce2.js"\n      crossorigin="anonymous"\n    ></script>\n    <link\n      rel="stylesheet"\n      type="text/css"\n      href="{{ url_for("static", filename="dashboard.css") }}"\n    />\n    <script\n      src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.0.2/echarts.min.js"\n      integrity="sha512-t9GZbGKCH5MuYUFsq5AdrhllT0kdnc2fNMizKDgLXBBXgHP2dXxjRPOzYJauAXW9OXLlSYELUqWD30k7cb0Mkg=="\n      crossorigin="anonymous"\n    ></script>\n    <script src="{{ url_for("static", filename="pos.js") }}"></script>\n    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>\n    <script src="{{ url_for("static", filename="jquery-3.6.0.js") }}"></script>\n    <title>' + name + '</title>\n  </head>\n  <body>\n    {% include "includes/_navbar.html" %} {% include "includes/_posFilter.html" %}')
    f.write(getKPIs(username, name, dashboardType, KPIs))
    f.write('\n<script type="text/javascript">\n  filterOption();\n  getData();\n</script>\n</body>\n</html>\n')
    f.close()


def addToSelector(username, name):
    f = open('templates/' + username + '/includes/_dashboards.html', "a")
    f.write('<div class="card"><input class="dashboard" id="dashboard" type=button onClick="parent.location=\'dashboard/' + name + '\'" value="' + name + '"></div>\n')
    f.close()

def addToUpload(username, name):
    f = open('templates/' + username + '/includes/_upload.html', "a")
    f.write('<div class="frame"><form action="/upload" method="POST" enctype="multipart/form-data"><div class="title"><h1>' + name.upper() + '</h1></div><div class="center"><div class="title"><h2>Drop file to upload</h2></div><div class="dropzone"><img src="http://100dayscss.com/codepen/upload.svg" class="upload-icon" /><input type="file" name="' + name + '" id="' + name + '" class="upload-input" /></div><button type="submit" class="btn" name="upload" value="upload_' + name + '">Upload file</button></div></form><div class="center download"><input class="btn download" type=button onClick="parent.location=\'download/' + name + '/template.csv\'"  value="Download Template"></div></div>\n')
    f.close()

def getKPIs(username, name ,dashboardType, KPIs):
    if(dashboardType == 'POS'):
        os.mkdir('CSV\\' + username + '\\' + name)
        with open('CSV\\' + username + '\\' + name + '\\template.csv', 'w') as fc:
            fc.write('date,country,city,store,brand,product,sold_units,onhand_units,sold_amount,onhand_amount')
            fc.close()
        pos = ''
        halfcard = '      <div class="halfcards">\n'
        card = '      <div class="cards">\n'
        for KPI in KPIs:
            print(KPI)
            if KPI == 'totalSales':
                halfcard += totalSales()
            elif KPI == 'averageInventoryAmount':
                halfcard += averageInventoryAmount()
            elif KPI == 'totalOnhandAmount':
                halfcard += totalOnhandAmount()
            elif KPI == 'salesPerStore':
                halfcard += salesPerStore()
            elif KPI == 'distinctProductsSold':
                halfcard += distinctProductsSold()
            elif KPI == 'outOfStock':
                halfcard += outOfStock()
            elif KPI == 'totalSalesPerDay':
                card += totalSalesPerDay()
            elif KPI == 'totalSalesPerCountry':
                card += totalSalesPerCountry()
            elif KPI == 'totalSalesPerCity':
                card += totalSalesPerCity()
            elif KPI == 'totalSalesPerStore':
                card += totalSalesPerStore()
            elif KPI == 'topProducts':
                card += topProducts()
            elif KPI == 'topBrands':
                card += topBrands()
            elif KPI == 'salesPercentageForBrand':
                card += salesPercentageForBrand() 
        halfcard+= '    </div>\n'
        pos+=halfcard
        card+= '    </div>\n'
        pos+=card
        return pos 
    return ''

def generate(username, name, dashboardType, KPIs):
    if os.path.isfile('templates/' + username + '\\' + name + '.html'):
        return False
    createFile(username, name, dashboardType, KPIs)
    addToSelector(username, name)
    addToUpload(username, name)
    return True