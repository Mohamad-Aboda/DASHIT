import ETL as etl
import pandas as pd

# Get Sum of column
def SUM_KPI(data, columns_names):
    colName = columns_names[0]
    total = data[colName].sum()
    return total

# Get column AVG
def AVG_KPI(data, columns_names):
    colName = columns_names[0]
    avg = data[colName].sum() / len(data)
    return avg

# Subtract two columns sum
def ADD(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    total = data[X].sum() + data[Y].sum()    
    return total

# Subtract two columns sum
def SUBTRACT(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    total = data[X].sum() - data[Y].sum()    
    return total


# Devide two columns sum
def DEVIDE(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    totalX = data[X].sum()
    totalY = data[Y].sum()   

    return totalX / totalY


# Devide two columns sum
def PERCENTAGE(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    totalX = data[X].sum()
    totalY = data[Y].sum()   

    return totalX * 100 / totalY



# location, columns_names as list, function_name as string
def create_KPI(location, columns_names, function_name, flag = 0):
    if(flag):
        data = location
    else:
        data = etl.loadData(location)
    if function_name == 'SUM':
        return SUM_KPI(data, columns_names)
    elif function_name == 'AVERAGE':
        return AVG_KPI(data, columns_names)
    elif function_name == 'ADD':
        return ADD(data, columns_names)
    elif function_name == 'SUBTRACT':
        return SUBTRACT(data, columns_names)
    elif function_name == 'DIVIDE':
        return DIVIDE(data, columns_names)
    elif function_name == 'PERCENTAGE':
        return PERCENTAGE(data, columns_names)
    else:
        return 0