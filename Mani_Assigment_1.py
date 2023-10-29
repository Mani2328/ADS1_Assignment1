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

df = pd.read_csv("SG_COE.csv")
df.dtypes

df['month'] = pd.to_datetime(df['month'])  # Convert df month to datetime format
#df.dtypes
df['year'] = df["month"].dt.year  # Create year columns as year
df['year'].astype({"year":int}); 

# Mean COE according to Category Type
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

