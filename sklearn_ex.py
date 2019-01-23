#! /usr/bin/env python3
#import the necessary module
from sklearn import preprocessing

# create the Labelencoder object
le = preprocessing.LabelEncoder()

#convert the categorical columns into numeric
encoded_value = le.fit_transform(["india", "paris", "paris", "tokyo", "amsterdam","india"])

print(encoded_value)
