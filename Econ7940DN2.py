# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:00:55 2024/01v

@author: dominic.ng
"""
import gc
import pandas as pd
import datetime as dt
'''Load All Fields
dtypeDict={ 'Invoice/Item Number':str,'Date':str, 'Store Number':'category', 'Store Name':'category', 'Address':'category',\
            'City':'category', 'Zip Code':'category', 'Store Location':'category', 'County Number':'category', 'County':'category', \
            'Category':'category', 'Category Name':'category', 'Vendor Number':'category', 'Vendor Name':'category',\
            'Item Number':'category', 'Item Description':'category', 'Pack':'category', 'Bottle Volume (ml)':float,\
            'State Bottle Cost':float, 'State Bottle Retail':float, 'Bottles Sold':float,
            'Sale (Dollars)':float, 'Volume Sold (Liters)':float, 'Volume Sold (Gallons)':float}
df=pd.read_csv("c:/Econ7940/Iowa_Liquor_Sales.csv",parse_dates=['Date'], dtype = dtypeDict)  #Test read the datafile to understand data
'''    

dtypeDict={ 'Invoice/Item Number':str,'Date':str, 'Store Number':'category', \
            'City':'category', 'Zip Code':'category', 'County Number':'category',  \
            'Category':'category',  'Vendor Number':'category', \
            'Item Number':'category', 'Pack':'category', 'Bottle Volume (ml)':float,\
            'State Bottle Cost':float, 'State Bottle Retail':float, 'Bottles Sold':float,
            'Sale (Dollars)':float, 'Volume Sold (Liters)':float}
colsList=['Invoice/Item Number','Date', 'Store Number', \
            'City', 'Zip Code', 'County Number',  \
            'Category',  'Vendor Number', \
            'Item Number', 'Pack', 'Bottle Volume (ml)',\
            'State Bottle Cost', 'State Bottle Retail', 'Bottles Sold',
            'Sale (Dollars)', 'Volume Sold (Liters)']
    
df=pd.read_csv("c:/Econ7940/Iowa_Liquor_Sales.csv",parse_dates=['Date'], dtype = dtypeDict, usecols=colsList)  #Test read the datafile to understand data

'''With nrows=100000 for testing purpopse
df=pd.read_csv("c:/Econ7940/Iowa_Liquor_Sales.csv",parse_dates=['Date'], dtype = dtypeDict, usecols=colsList, nrows=100000)  #Test read the datafile to understand data
'''

categoryList=['Store Number', \
            'City', 'Zip Code', 'County Number',  \
            'Category',  'Vendor Number', \
            'Item Number', 'Pack']

for item in categoryList:
    df[item]=df[item].str.upper().str.strip().str.replace(" ","").astype('category')
    gc.collect()