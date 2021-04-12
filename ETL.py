# importing libraries
import os
import json
import numpy as np
import pandas as  pd

# Get extentions of the file
def getExt(path):
    return path.split('.')[1]


# load Data
def loadData(location):


    # create list of DataFrames
    dataHouse = []
    path = os.getcwd()+'\\CSV\\'+location                               # Dataset path for a user 
    fileList = os.listdir(path)                                         # get all data uploaded for a user
    for filename in fileList:
        if filename == 'template.csv':
            continue
        ext = getExt(filename)                                           # Get file extentions
        tempPath = path + '\\'  + filename                               # Get file path to read it

        # Check DataType and Read it
        if ext == 'csv':
            df = pd.read_csv(tempPath)
        elif ext == 'xlsx':
            df = pd.read_excel(tempPath, engine='openpyxl')
        
        df = cleanData(df)                                               # Clean the data
        dataHouse.append(df)                                             # add The data to the data wareHouse


    return dataHouse

# Clean  Rows with NaN values
def cleanData(df):
    df.dropna(axis = 0, inplace = True)
    return df