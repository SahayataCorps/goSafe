# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:16:42 2019

@author: GameZone
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import average_precision_score, precision_recall_curve, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.utils.fixes import signature
import re
from datetime import date, datetime

tokens = {
        "nmDomain":[],
        "mDomain":[],
        "nmPath":[],
        "mPath":[],
        "nmReg":[],
        "mReg":[],
        "nmWhois":[],
        "mWhois":[]
        }
#Does not use it
def getRight(Xd):
    totaliter = len(Xd)
    mal = list(map(int,Xd['malicious']))
    domain = list(map(str,Xd['domainToken']))
    path = list(map(str,Xd['pathToken']))
    reg = list(map(str,Xd['registrar']))
    whoisS = list(map(str,Xd['whoisServer']))
    nameS = list(Xd['nameServer'])   
    for i in range(totaliter):
        if mal[i] == 0:
            for x in domain[i].split(','):
                tokens['nmDomain'].append(x)
            for x in path[i].split(','):
                tokens['nmPath'].append(x)
            for x in reg[i].split(','):
                tokens['nmReg'].append(x)
            x = whoisS[i].split('.')[1:]
            for y in x:
                tokens['nmWhois'].append(y)

        else:
            for x in domain[i].split(','):
                tokens['mDomain'].append(x)
            for x in path[i].split(','):
                tokens['mPath'].append(x)
            for x in reg[i].split(','):
                tokens['mReg'].append(x)
            x = whoisS[i].split('.')[1:]
            for y in x:
                tokens['mWhois'].append(y)
                

df=pd.read_csv('final.csv')
df.head()
            
nmDomain=pd.read_fwf('nmDomain.txt',names=["nmDomain"],header=None)
nmDomain_probab=1/(len(nmDomain))
mDomain=pd.read_fwf('mDomain.txt')
mDomain_probab=1/(len(mDomain))
nmPath=pd.read_fwf('nmPath.txt')
nmPath_probab=1/(len(nmPath))
nmReg=pd.read_fwf('nmReg.txt')
nmReg_probab=1/(len(nmReg))
nmDomain=pd.read_fwf('nmDomain.txt')
nmDomain_probab=1/(len(nmDomain))
mPath=pd.read_fwf('mPath.txt')
mPath_probab=1/(len(mPath))
mReg=pd.read_fwf('mReg.txt')
mReg_probab=1/(len(mReg))
mWhois=pd.read_fwf('mWhois.txt')
mWhois_probab=1/(len(mWhois))
nmWhois=pd.read_fwf('nmWhois.txt')
nmWhois_probab=1/(len(nmWhois))


V=['nmDomain','mDomain']
V_dict = {'nmDomain':nmDomain,'mDomain':mDomain} 
T=[nmDomain_probab,mDomain_probab]
W=['domainToken']


for k in V:
    df[k]= 0.0


for i in range(0,1005):
    U=0
    for k in W:
        
        for j in ((str(df.loc[i,k])).split(",")):
            if j in V_dict[V[U]].values:
                df.loc[i,V[U]]+= T[U]
                print(i)
            elif j in V_dict[V[U+1]].values:
                df.loc[i,V[U+1]]+=T[U+1]
                print(i)
        U+=2


X=df.drop('malicious',axis=1)
X=X.drop('hostname', axis=1)
X=X.drop('primaryDomain', axis=1)
X=X.drop('topLevelDomain', axis=1)
X=X.drop('ipaddress', axis=1)
X=X.drop('protocol', axis=1)
#X=X.drop('creationDate', axis=1)
#X=X.drop('age', axis=1)
#X=X.drop('registrar', axis=1)
#X=X.drop('whoisServer', axis=1)
#X=X.drop('expiration', axis=1)
#X=X.drop('nameServer', axis=1)
#X=X.drop('country', axis=1)
#X=X.drop('name', axis=1)
X=X.drop('path', axis=1)
X=X.drop('query', axis=1)
X=X.drop('noOfQuery', axis=1)
X=X.drop('pathToken', axis=1)
for k in W:
    X=X.drop(k,axis=1)

Y=df['malicious']
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.20)

#svclassifier = SVC(kernel='linear')
#svclassifier.fit(X_train, y_train)

#y_pred = svclassifier.predict(X_test)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

avgprecision = average_precision_score(y_test, y_pred)
print(" average precision recall score : {0:0.2f}".format(avgprecision))
print(confusion_matrix(y_test, y_pred))