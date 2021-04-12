import json
import ETL as etl
import pandas as pd


# To create a bar-char
def CHART(data, columns_names):
    groupByCol = columns_names[0]
    groupCol = columns_names[1]
    
    result = data[0].groupby(groupByCol)[groupCol].sum()
    result -= result
    
    for df in data:
        result = result.add(df.groupby(groupByCol)[groupCol].sum(), fill_value = 0)
    return result.to_json(orient = 'split')



# location, columns_names as list, function_name as string
def create_chart(location, columns_names, chart_type, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)
    if 'CHART' in chart_type:
        return CHART(data, columns_names)

 