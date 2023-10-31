# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 00:48:46 2023

@author: 65947
"""

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd
from datetime import datetime 

# Read SG_COE csv file
df = pd.read_csv("SG_COE.csv")
df.dtypes

# change the month colum to date time format
df['month'] = pd.to_datetime(df['month'])  # Convert df month to datetime format
#df.dtypes
df['year'] = df["month"].dt.year  # Create year columns as year
df['year'].astype({"year":int}); 
df

# create a new column "COE_Colletion" with bids_success * premium
df["COE_Collection"] = df["bids_success"] * df["premium"]
df

# Calculate the mean of COE each year by Category

CatA = df[df['vehicle_class'] == "Category A"]
CatA_mean = CatA.groupby('year')[["premium"]].mean()
CatB = df[df['vehicle_class'] == "Category B"]
CatB_mean = CatB.groupby('year')[["premium"]].mean()
CatC = df[df['vehicle_class'] == "Category C"]
CatC_mean = CatC.groupby('year')[["premium"]].mean()
CatD = df[df['vehicle_class'] == "Category D"]
CatD_mean = CatD.groupby('year')[["premium"]].mean()
CatE = df[df['vehicle_class'] == "Category E"]
CatE_mean = CatE.groupby('year')[["premium"]].mean()

plt.title("Mean Premium of COE (SGD)", fontsize = 10)
#plt.annotate('ABSD 5%', xy=(2018.7, 480000), xytext=(2018.7, 500000),     
                #arrowprops=dict(facecolor='black', shrink=0.05))

        
plt.plot(CatA_mean, label = "CatA") 
plt.plot(CatB_mean, label = "CatB")
plt.plot(CatC_mean, label = "CatC")
plt.plot(CatD_mean, label = "CatD")
plt.plot(CatE_mean, label = "CatE")

plt.legend()
plt.show()


COE_Revenue = df.groupby("vehicle_class")["COE_Collection"].sum()
COE_Revenue.plot(kind="bar")
plt.title("Revenue in Billion - SGD Dollars")
plt.ylabel("Revenue Collection from 2010 to 2023")
plt.show()


# Percentage of COE collection over total COE Collected from 2012 to 2023

# Total COE Collected
COE_Total = df["COE_Collection"].sum()
COE_Total

# Percentage of COE collection for Category A
CatA = df[df['vehicle_class'] == "Category A"]
CatA_sum = CatA["COE_Collection"].sum()
CatA_Percentage = (CatA_sum / COE_Total * 100)
CatA_Percentage

# Percentage of COE collection for Category B
CatB = df[df['vehicle_class'] == "Category B"]
CatB_sum = CatB["COE_Collection"].sum()
CatB_Percentage = (CatB_sum / COE_Total * 100)
CatB_Percentage

# Percentage of COE collection for Category C
CatC = df[df['vehicle_class'] == "Category C"]
CatC_sum = CatC["COE_Collection"].sum()
CatC_Percentage = (CatC_sum / COE_Total * 100)
CatC_Percentage

# Percentage of COE collection for Category D
CatD = df[df['vehicle_class'] == "Category D"]
CatD_sum = CatD["COE_Collection"].sum()
CatD_Percentage = (CatD_sum / COE_Total * 100)
CatD_Percentage

# Percentage of COE collected for Category E
CatE = df[df['vehicle_class'] == "Category E"]
CatE_sum = CatE["COE_Collection"].sum()
CatE_Percentage = (CatE_sum / COE_Total * 100)
CatE_Percentage

Pie_Data = {'Cat_A': 38.929, 'Cat_B': 35.479 , 'Cat_3': 7.952,
             'Cat_D':2.062, 'Cat_E':15.575 }
Percentage_Data = pd.Series(Pie_Data)
Percentage_Data

labels = 'Cat_A', 'Cat_B', 'Cat_C', 'Cat_D', 'Cat_E'
plt.pie(Percentage_Data, labels = labels, autopct='%1.1f%%',
       startangle=90)
plt.title("Percentage Revenve - By Category")
plt.show()






