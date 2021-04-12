import json
import ETL as etl
import pandas as pd
import KPIs as kp

# Total sales per day : line-chart
def totalsales_per_day(location):
    data = etl.loadData(location)
    result = data[0].groupby('date')['sold_amount'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('date')['sold_amount'].sum()])
    return result[1:].to_json(orient = 'split')


# Total sales per country : bar-chart
def totalsales_per_country(location):
    data = etl.loadData(location)
    result = data[0].groupby('country')['sold_amount'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('country')['sold_amount'].sum(), fill_value = 0)
    return result.to_json(orient = 'split')


# Total sales per City : bar-chart
def totalsales_per_city(location):
    data = etl.loadData(location)
    result = data[0].groupby('city')['sold_amount'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('city')['sold_amount'].sum(), fill_value = 0)
    return result.to_json(orient = 'split')


# Total sales per store : bar-chart
def totalsales_per_store(location):
    data = etl.loadData(location)
    result = data[0].groupby('store')['sold_amount'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('store')['sold_amount'].sum(), fill_value = 0)
    return result.to_json(orient = 'split')



# Top products : number of units solds bar-chart
def top_products(location):
    data = etl.loadData(location)
    result = data[0].groupby('product')['sold_units'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('product')['sold_units'].sum(), fill_value = 0)
    return result.sort_values(ascending=False).head().to_json(orient = 'split')


# Top Brand : number of units solds bar-chart
def top_brands(location):
    data = etl.loadData(location)
    result = data[0].groupby('brand')['sold_units'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('brand')['sold_units'].sum(), fill_value = 0)
    return result.sort_values(ascending=False).head().to_json(orient = 'split')


# Sales Percentage : Pie-chart
def sales_percentage_for_brand(location):
    data = etl.loadData(location)
    result = data[0].groupby('brand')['sold_amount'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('brand')['sold_amount'].sum(), fill_value = 0)
    result = round(result * 100 / int(kp.total_sales(data, 1)[0]))
    return result.to_json(orient = 'split')
