# Classification template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('final.csv')

df= pd.read_csv('final.csv')
df.head()
X=df.drop('malicious',axis=1)
X=X.drop('protocol', axis=1)
X=X.drop('hostname', axis=1)
X=X.drop('topLevelDomain', axis=1)
X=X.drop('primaryDomain', axis=1)
X=X.drop('path', axis=1)
X=X.drop('pathLength', axis=1)
X=X.drop('query', axis=1)
X=X.drop('ipaddress', axis=1)
#X=X.drop('creationDate', axis=1)
#X=X.drop('age', axis=1)
#X=X.drop('expiration', axis=1)
#X=X.drop('nameServer', axis=1)
X=X.drop('domainToken', axis=1)
#X=X.drop('registrar', axis=1)
X=X.drop('pathToken', axis=1)
#X=X.drop('whoisServer', axis=1)
#X=X.drop('country', axis=1)
#X=X.drop('name', axis=1)
X=X.drop('noOfQuery', axis=1)


Y=df.iloc[:,24].values

X = X.iloc[:,:].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.20)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Fitting Random Forest Classification to the Training set

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 30, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

import pickle
f = open('model.pkl', 'wb')
pickle.dump(classifier,f)
f.close()

