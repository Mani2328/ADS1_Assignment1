# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 00:48:46 2023

@author: 65947
"""
# Import the python package
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd
from datetime import datetime 

# Read SG_COE csv file
df = pd.read_csv("SG_COE.csv")

# change the month column to date time format
df['month'] = pd.to_datetime(df['month']) 
df['year'] = df["month"].dt.year  # Create year columns as year
df['year'].astype({"year":int}); 
df["COE_Collection"] = df["bids_success"] * df["premium"]

# Update simple variable for COE category
A = "Category A"
B = "Category B"
C = "Category C"
D = "Category D"
E = "Category E"

def mean(df, A):
    """ the function mean calculate the 
    mean COE value for each year, the input 
    variables are data frame and Category """
    
    A = df[df['vehicle_class'] == A]
    Cat_mean = A.groupby('year')[["premium"]].mean()
    return Cat_mean

# Calculate mean values for each year using function mean
CatA_mean = mean(df, A)
CatB_mean = mean(df, B)
CatC_mean = mean(df, C)
CatD_mean = mean(df, D)
CatE_mean = mean(df, E)

# Line plot of COE price from 2010 to 2023
plt.figure(figsize=(10,5))     
plt.plot(CatA_mean, label = "CatA") 
plt.plot(CatB_mean, label = "CatB")
plt.plot(CatC_mean, label = "CatC")
plt.plot(CatD_mean, label = "CatD")
plt.plot(CatE_mean, label = "CatE")
plt.ylabel("COE Mean Price - ($SGD)")
plt.xlabel("Year")
plt.xlim(2010, 2023)
plt.title("COE Price from 2010 to 2023", fontsize = 15)
plt.annotate('COE Quota cut by 30%', xy=(2020, 40000), xytext=(2015.5, 60000),     
                arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend()
plt.show()

# Bar plot Revenue collected by each COE Category
plt.figure(figsize=(10,5))
COE_Revenue = df.groupby("vehicle_class")["COE_Collection"].sum()
COE_Revenue.plot(kind = "bar", color = "red", rot = 45)
plt.title("Revenue in Billion - SGD Dollars")
plt.ylabel("Revenue Collection from 2010 to 2023")
plt.show()

# Total COE Collection from all Category
COE_Total = df["COE_Collection"].sum()
COE_Total

# Function percentage to calculate the % for each category of the total COE

def percentage(df, A):
    """ the function percentage calculate the
    percentage of each category, input cariable 
    for the function is the data and category variable """
    
    A = df[df['vehicle_class'] == A]
    Cat_sum = A["COE_Collection"].sum()
    Cat_Percentage = (Cat_sum / COE_Total * 100)
    return Cat_Percentage

Category_A = percentage(df, A)
Category_B = percentage(df, B)
Category_C = percentage(df, C)
Category_D = percentage(df, D)
Category_E = percentage(df, E)

""" The pie chart shows the percentag of revenue
collected from each COE category"""
plt.figure(figsize=(10,5))
Pie_Data = {'Cat_A': Category_A, 'Cat_B': Category_B, 'Cat_3': Category_C,
             'Cat_D':Category_D, 'Cat_E': Category_E}
Percentage_Data = pd.Series(Pie_Data)

labels = 'Cat_A', 'Cat_B', 'Cat_C', 'Cat_D', 'Cat_E'
plt.pie(Percentage_Data, labels = labels, autopct='%1.1f%%',
       startangle=90)
plt.title("Percentage of Revenue Collected from each Category", fontsize=10)
#plt.subtitle("Total Revenve Collected SGD 40.15 Billion Dollars")
plt.show()









