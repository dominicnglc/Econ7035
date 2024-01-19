#TESTING
import pandas as pd
import datetime as dt
import gc
#dtypeDict={ 'State Bottle Cost':str, 'State Bottle Retail':str, 'Bottles Sold':str,
#            'Sale (Dollars)':str, 'Volume Sold (Liters)':str, 'Volume Sold (Gallons)':str}
df=pd.read_csv("c:/Econ7940/Iowa_Liquor_Sales.csv", usecols=['Zip Code','Item Number'])  #Test read the datafile to understand data
#df.Date=df.Date.dt.date
'''
print(df.info())
counter=1
for key in dtypeDict:
    #instance or __name_
    print('Column Number:'+str(counter))
    if dtypeDict[key].__name__=='str':
      print("  Name: " + str(key))
      print("  Null: " + str(df[key].isnull().sum()))
      print("  Non:Null: " + str(df[key].value_counts().sum()))
      print("  Uniqued: "+str(df[key].str.upper().str.strip().str.replace(" ","").drop_duplicates().count()))

    if dtypeDict[key].__name__=='float':
      print("  Name: " + str(key))
      print("  Null: " + str(df[key].isnull().sum()))
      print("  Non:Null: " + str(df[key].value_counts().sum()))
      print("  Min: " + str(df[key].min()))
      print("  Max: " + str(df[key].max()))
      print("  Average: " + str(df[key].mean()))
      print("  SD: " + str(df[key].std()))
            
    counter+=1
    print("")
    gc.collect()
    
df['Zip Code'].str.len().max()
Out[6]: 5.0

df['Zip Code'].str.len().min()
Out[7]: 5.0    

df['Zip Code'].str.isnumeric()==False
'''