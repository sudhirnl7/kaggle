#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:49:13 2017

@author: sudhir
"""
"""" Zillow house price prediction

The objective of the compitation is to estimate some thing called logerror, which zillow estimate of sell price of a house
and actual sale price.We won't be given the actual Zestimate or price. The point is to figure out what sorts of sales Zillow is good at estimating, and what sort they are bad at estimating
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sy

# =============================================================================
# Read data set
# =============================================================================
train = pd.read_csv('train_2016_v2.csv')
properties= pd.read_csv('properties_2016.csv',low_memory=False)

for c,dtype in zip(properties.columns,properties.dtypes):
    if dtype == np.float64:
        properties[c]=properties[c].astype(np.float32)
train.head()
properties.head()

train_df= pd.merge(train,properties,on='parcelid',how='left')
train_df.info()
train_df.fillna(0)

# =============================================================================
# #traget variable
# =============================================================================
sns.distplot((train['logerror']))

for c in train_df.dtypes[train_df.dtypes == object].index.values:
    train_df[c] = (train_df[c] == True)
#

X = train_df.drop(['parcelid','logerror','transactiondate', 
                         'propertyzoningdesc', 'propertycountylandusecode'],axis=1)
y = train_df['logerror'].values.astype(np.float64)

# =============================================================================
# 
# =============================================================================
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
lm= LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.7,random_state=100)

# =============================================================================
# Model
# =============================================================================
lm.fit(x_train.fillna(0),y_train)
prd=lm.predict(x_test.fillna(0))
