#! /usr/bin/env python3

# Import pandas module
import pandas as pd

# import the seaborn module
import seaborn as sns

# import the matplotlib module
import matplotlib.pyplot as plt

# Import the preprocessing module
from sklearn import preprocessing

#import the necessary module ## To prepare Training and test data set
from sklearn.model_selection import train_test_split

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
for Training and test part , Lets prepare dataset for train and test
"""


#select columns other than 'Opportunity Number','Opportunity Result'
cols = [col for col in sales_data.columns if col not in ['Opportunity Number','Opportunity Result']]

#dropping the 'Opportunity Number'and 'Opportunity Result' columns
data = sales_data[cols]

#assigning the Oppurtunity Result column as target
target = sales_data['Opportunity Result']

data.head(n=2)

#split data set into train and test sets
data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.30, random_state = 10)

"""
Building ML model:

machine_learning_map we can try out the below mentioned algorithms.

- Naive Bayes
- Linear SVC
- K-Neighbours Classifier
"""

#import the necessary modules
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#create an object of type LinearSVC
svc_model = LinearSVC(random_state=0)

#train the algorithm on training data and predict using the testing data
pred = svc_model.fit(data_train, target_train).predict(data_test)

#print the accuracy score of the model
print ("****-------------------**** ------------ **** --------------****")
print("LinearSVC accuracy : ",accuracy_score(target_test, pred, normalize = True))
print ("****-------------------**** ------------ **** --------------****")



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
