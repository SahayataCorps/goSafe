import pandas as pd
import requests
import csv
from QuikKool import MaliNon

data = pd.read_csv('cleanse.csv', header=None)
a = 2
X = data.iloc[:,0].values
Y = data.iloc[:,1].values
working = []

for i in range(a):
    url = X[i]
    b = MaliNon()
    print(url)
    if (b.check(url)):
        try:
            b.reset()
            lex = b.Features(url)
            b.getSource(url)
            working.append(b.finalAppend(url)+lex + [int(Y[i])])
            print(i)
        except:
            print("error")
print(working)
with open("fe.csv", 'wb') as fil:
    writer = csv.writer(fil, delimiter=',')
    writer.writerows(working)


