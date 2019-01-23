#! /usr/bin/env python3

# Import pandas module
import pandas as pd

# import the seaborn module
import seaborn as sns

# import the matplotlib module
import matplotlib.pyplot as plt

# Import the preprocessing module
from sklearn import preprocessing

# create the Labelencoder object
le=preprocessing.LabelEncoder() 

# Read CSV files
sales_data=pd.read_csv("WA_Fn-UseC_-Sales-Win-Loss.csv")

print ("------------------- ------------ --------------")
print ("List of Attributes from sales data: ")
print ("------------------- ------------ --------------")

print (sales_data.dtypes)
print ("------------------- ------------ --------------")

print ("------------------- ------------ --------------")
print ("sales_data before encoding: ")
print ("------------------- ------------ --------------")

print("Supplies Subgroup' : ",sales_data['Supplies Subgroup'].unique())
print("Region : ",sales_data['Region'].unique())
print("Route To Market : ",sales_data['Route To Market'].unique())
print("Opportunity Result : ",sales_data['Opportunity Result'].unique())
print("Competitor Type : ",sales_data['Competitor Type'].unique())
print("'Supplies Group : ",sales_data['Supplies Group'].unique())

print ("------------------- ------------ --------------")
print ("sales_data after encoding: ")
print ("------------------- ------------ --------------")
#convert the categorical columns into numeric
sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])

print("Supplies Subgroup' : ",sales_data['Supplies Subgroup'].unique())
print("Region : ",sales_data['Region'].unique())
print("Route To Market : ",sales_data['Route To Market'].unique())
print("Opportunity Result : ",sales_data['Opportunity Result'].unique())
print("Competitor Type : ",sales_data['Competitor Type'].unique())
print("'Supplies Group : ",sales_data['Supplies Group'].unique())



"""
# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)

# setting the plot size for all plots
sns.set(rc={'figure.figsize':(16.7,13.27)})

# create a countplot
# sns.countplot('Region',data=sales_data,hue = 'Region')

# create a countplot using violinplot() method
sns.violinplot(x="Opportunity Result",y="Client Size By Revenue", hue="Opportunity Result",data=sales_data);

# Remove the top and down margin
sns.despine(offset=10, trim=True)

# display the plot
plt.show()
"""
