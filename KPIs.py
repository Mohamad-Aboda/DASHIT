import pandas as pd
import ETL as etl
import Filtering
import json

# Total Sales
# return as list : total_amount, amount of current day, amount of last day  
def total_sales(location, flag=0):
    if(flag):
        data = location
    else:
        data=etl.loadData(location)
    
    total = 0
    for df in data:
        total += df['sold_amount'].sum()

    now = 0
    if len(data) > 0: 
        now = data[-1]['sold_amount'].sum()
    
    last = 0    
    if len(data) > 1:
        last = data[-2]['sold_amount'].sum()
    result = {}
    result['data'] = [str(total), str(now), str(last)]
    return result['data']


# Average Sales Per Stores : Total Sales / Active Stores
# Return as list: average sales per store now then last day
def sales_per_store(location, flag=0):
    if(flag):
        data = location
    else:
        data=etl.loadData(location)

    no_of_stores_now = 0
    for df in data:
        no_of_stores_now = max(no_of_stores_now, len(df['store'].unique()))
    
    no_of_stores_last = 0
    for df in data[:-1]:
        no_of_stores_last = max(no_of_stores_last, len(df['store'].unique()))

    total = total_sales(data, 1)
    try:
        result_now = round(int(total[0]) / no_of_stores_now)
    except:
        result_now = 0
    try:
        result_last = round((int(total[0]) - int(total[1])) / no_of_stores_last)
    except:
        result_last = 0
    result = {}
    result['data'] = [str(result_now), str(result_last)] 
    return result['data']


# Total On-Hand Amount : Sum of (last period only) [On-Hand Amount]
# return as list number of total hand amount now, then last day
def total_onhand_amount(location, flag=0):
    if(flag):
        data = location
    else:
        data=etl.loadData(location)

    no_of_days = len(data)

    now = data[no_of_days-1]['onhand_amount'].sum()
    last = data[no_of_days-2]['onhand_amount'].sum()
    result = {}
    result['data'] = [str(now), str(last)] 
    return result['data']



# Total On-Hand Amount : Sum of (last period only) [On-Hand units]
# return as list number of total hand units now, then last day
def total_onhand_units(location, flag=0):
    if(flag):
        data = location
    else:
        data=etl.loadData(location)

    no_of_days = len(data)

    now = data[no_of_days-1]['onhand_units'].sum()
    last = data[no_of_days-2]['onhand_units'].sum()
    result = {}
    result['data'] = [str(now), str(last)] 
    return result['data']



# Average Inventory Amount : Total On-Hand Amount over the periodDivided byNumber of Dates
def average_inventory_amount(location, flag=0):
    if(flag):
        data = location
    else:
        data=etl.loadData(location)

    total_amount_last = 0
    for df in data[:-1]:
        total_amount_last += df['onhand_amount'].sum()

    total_amount_now = total_amount_last + data[-1]['onhand_amount'].sum()
    no_of_days = len(data)

    # Calculate the avergae for now and last day
    now = 0
    if no_of_days > 0:
        now = round(total_amount_now / no_of_days)
    
    last = 0
    if no_of_days > 1:
        last =  round(total_amount_last / (no_of_days-1))
    result = {}
    result['data'] = [str(now), str(last)] 
    return result['data']


# Distinct Products Sold : Count Distinct of [Product]
def ditinct_products_sold(location, flag=0):
    
    if(flag):
        data = location
    else:
        data=etl.loadData(location)

    total_df = data[0]['product']
    
    for df in data[:-1]:
        total_df = pd.concat([total_df, df['product']])

    last = len(total_df.unique())
    total_df = pd.concat([total_df, data[-1]['product']])
    now = len(total_df.unique())
    result = {}
    result['data'] = [str(now), str(last)] 
    return result['data']


# Out-of-Stock Positions : Sum of IF [On-Hand Units]=0 THEN 1 END
def out_of_stock(location, flag=0):
    if(flag):
        data = location
    else:
        data=etl.loadData(location)

    df = data[-1]
    now = df['onhand_units'][df['onhand_units'] == 0].count()
    try:
        df = data[-2]
        last= df['onhand_units'][df['onhand_units'] == 0].count()
    except:
        last = 0
    result = {}
    result['data'] = [str(now), str(last)] 
    return result['data']