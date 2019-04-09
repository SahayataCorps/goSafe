from LexalFeature import LexicalFeatures
import sys
import requests
import json 
import pandas as pd

X_train = pd.read_csv("mean.csv")
class Finale:
    finalle = []
    headers = [
       'hostnameLength',
       'topLevelDomainLength',
       'primaryDomainLength',
        "containsIp",
        "no_of_dots",
        "length_of_url",
        "token_count",
        "avg_token_length",
        "path_token_count",
        "avg_path_token",
        "domain_token_count",
        "largest_domain",
        "avg_domain_token",
        ]
    #finalle.append(headers)
    url = ''
    mal = 0

    def getFeatures(self,u,m):
        self.url = u
        self.mal = m
        lf = LexicalFeatures(self.url,self.mal)
        lf.fillDetails()
        lfl = lf.returnFeature()

        
        sumup = lfl
        self.finalle.append(sumup)
        

a = Finale()
url = sys.argv[1]

if url.startswith("http"):
    u = url
else:
    u = "http://" + url
a.getFeatures(u, 0)
dt = a.finalle

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train.iloc[:,1:].values)
dtt = sc.transform(dt)
f = dtt.tolist()
f = [round(x,5) for x in f[0]]



data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": [ "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12"],
                    "Values": [f , ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/96c958c826904849b74df9dcee941f58/services/5b162bec4dc34142b686b47709562aba/execute?api-version=2.0&details=true'
api_key = 'Avc9snJN5AlKGGcIAl/Ir4gCUmbuXiQPpWFxofapXRmgTEvkwxkSCMxYxf1PCIgCRqADuOlBZ42J+PWRMwmWzQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
  
# sending post request and saving response as response object 
r = requests.post(url = url, headers = headers, data = body) 
pastebin_url = r
print(pastebin_url.text)

