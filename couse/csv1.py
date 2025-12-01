import pandas as pd
from pandas import read_csv

#read csv
newCSV=pd.read_csv("testdata.csv",names=["vk","kk","sr","mm"])
print(newCSV)
#write csv
newCSV.to_csv("testdata1.csv")
newCSV=pd.read_csv("testdata1.csv")
print(newCSV)
