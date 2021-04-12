import json
import ETL as etl
import pandas as pd
import FinancialKPIs as kp

# Total Revenue per Month : line-chart
def total_revenue_per_month(location):
    data = etl.loadData(location)

    result = data[0].groupby('Month')['revenues'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('Month')['revenues'].sum()])
    
    return result[1:].to_json(orient = 'split')


# Total Revenue per company : bar-chart
def total_revenue_per_company(location):
    data = etl.loadData(location)

    result = data[0].groupby('Company')['revenues'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('Company')['revenues'].sum()])
    
    return result[1:].to_json(orient = 'split')


# COGS per company : bar-chart
def COGS_per_company(location):
    data = etl.loadData(location)

    result = data[0].groupby('Company')['COGS'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('Company')['COGS'].sum()])
    
    return result[1:].to_json(orient = 'split')


# Gross margin per company : bar-chart
def gross_margin_per_company(location):
    data = etl.loadData(location)

    result = data[0].groupby('Company')['COGS'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('Company')['COGS'].sum()])
    
    return result[1:].to_json(orient = 'split')


# Gross margin percentage per company : bar-chart
def gross_margin_percentage_per_company(location):
    data = etl.loadData(location)
    
    result = data[0].groupby('Company')['revenues'].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby('Company')['revenues'].sum(), fill_value = 0)
        result = result.subtract(df.groupby('Company')['COGS'].sum(), fill_value = 0)

    result = result * 100 / kp.total_revenues(location = data, flag=1)
    return result.to_json(orient = 'split')


# OPEX per company : bar-chart
def OPEX_per_company(location):
    data = etl.loadData(location)

    result = data[0].groupby('Company')['OpEx'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('Company')['OpEx'].sum()])
    
    return result[1:].to_json(orient = 'split')


# OPEX_to_revenue per company : bar-chart
def OPEX_to_revenue_per_company(location):
    data = etl.loadData(location)

    result = data[0].groupby('Company')['OpEx'].sum()
    for df in data:
        result = pd.concat([result, df.groupby('Company')['OpEx'].sum()])
    
    result = result * 100 / kp.total_revenues(location = data, flag=1)
    return result[1:].to_json(orient = 'split')


