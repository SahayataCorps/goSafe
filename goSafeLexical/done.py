import pandas as pd

df = pd.read_csv("final.csv")
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]

X = X.apply(pd.to_numeric)

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
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
X_test = sc.transform(X_test)
