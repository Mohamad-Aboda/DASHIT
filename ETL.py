import os
import json
import numpy as np
import pandas as  pd

# Get extentions of the file
def getExt(path):
    return path.split('.')[1]


# load Data
def loadData(location):

    path = os.getcwd()+'\\CSV\\'+location                               # Dataset path for a user 
    fileList = os.listdir(path)                                         # get all data uploaded for a user

    isLoaded = False
    for filename in fileList:

        # Dont load the template
        if filename == 'template.csv':
            continue
        
        # Get the extinsion
        ext = getExt(filename)                                           # Get file extentions
        tempPath = path + '\\'  + filename                               # Get file path to read it

        # Check DataType and Read it
        if ext == 'csv':
            df = pd.read_csv(tempPath)
        elif ext == 'xlsx':
            df = pd.read_excel(tempPath, engine='openpyxl')
        
        # Clean data before loading
        df = cleanData(df)                                               # Clean the data

        # Concat all data
        if isLoaded == False:
            allData = df
            isLoaded = True  
        else:
            allData = pd.concat([allData, df])


    if allData.columns[0] == 'date':
        dataHouse = []
        allData = allData.drop_duplicates()
        dates = allData['date'].unique()
        dates.sort()

        for date in dates:
            df = allData[allData['date'] == date]
            dataHouse.append(df)
        
        
    elif allData.columns[0] == 'month':
        dataHouse = []
        allData = allData.drop_duplicates()
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

        for month in months:
            df = allData[allData['month'] == month]
            dataHouse.append(df)
        
    else:
        allData.drop_duplicates()
        dataHouse = allData

    return dataHouse

# Clean  Rows with NaN values
def cleanData(df):
    df.dropna(axis = 0, inplace = True)
    return df