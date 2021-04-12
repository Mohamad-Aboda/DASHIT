import pandas as pd
import ETL as etl


# Total Revenues : sum of revenues
def total_revenues(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    total = 0
    for df in data:
        total += df['revenues'].sum()
    return total


# COGS : sum of COGS
def COGS(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    total = 0
    for df in data:
        total += df['COGS'].sum()
    return total


# OpEx : sum of OpEx
def OpEx(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    total = 0
    for df in data:
        total += df['OpEx'].sum()
    return total


# Gross Margin : Total Revenues Minus COGS
def gross_margin(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    return total_revenues(location =  data,flag = 1) - COGS(location = data,flag = 1)


# Gross Margin % : Gross Margin / Revenues (%)
def gross_margin_percentage(location, flag = 0):
    
    if(flag):
        data = location
    else:
        data = etl.loadData(location)
    
    return round(gross_margin(location = data, flag = 1) / total_revenues(location = data, flag = 1), 3)


# OpEx to Revenues ratio : OpEx / Total Revenues
def OpEx_to_revenue(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    return round(OpEx(location = data, flag = 1) / total_revenues(location = data, flag=1), 3)


# Deprec & Amort : Sum of [Depreciations & Amortizations]
def deprec_and_amort(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    total = 0
    for df in data:
        total += df['Depreciations'].sum()
    return total


# Operating Income : Gross Margin Minus Opex & Deprec. & Amort.
def operating_income(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)

    return round(gross_margin(location = data, flag=1) / (OpEx(location = data, flag = 1) + deprec_and_amort(location = data, flag=1)), 3)


# Operating Income % : Operating Income / Total Revenues
def operating_income_percentage(location, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)
    
    return "{:.7f}".format(operating_income(location = data, flag=1) / total_revenues(location = data, flag = 1)*100, 7)
