import ETL as etl
import pandas as pd

# Get Sum of column
def SUM_KPI(data, columns_names):
    colName = columns_names[0]
    total = 0
    for df in data:
        total += df[colName].sum()

    return total

# Get column AVG
def AVG_KPI(data, columns_names):
    colName = columns_names[0]

    avg = 0
    for df in data:
        avg += df[colName].sum() / len(df)
    avg /= len(data)
    return avg

# Subtract two columns sum
def ADD(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    total = 0
    for df in data:
        total += df[X].sum() + df[Y].sum()    

    return total

# Subtract two columns sum
def SUBTRACT(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    total = 0
    for df in data:
        total += df[X].sum() - df[Y].sum()    

    return total


# DIvide two columns sum
def DIVIDE(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    totalX = 0
    totalY = 0
    for df in data:
        totalX += df[X].sum()
        totalY += df[Y].sum()   

    return totalX / totalY


# DIvide two columns sum
def PERCENTAGE(data, columns_names):
    X = columns_names[0]
    Y = columns_names[1]

    totalX = 0
    totalY = 0
    for df in data:
        totalX += df[X].sum()
        totalY += df[Y].sum()   

    return totalX * 100 / totalY



# location, columns_names as list, function_name as string
def create_KPI(location, columns_names, function_name, flag = 0):
    print(location)
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