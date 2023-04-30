import pandas as pd
file = open("table.txt","r")
tables = pd.read_html(file)
tab = tables[0].to_dict()
resource = ""
importstr =""
for index in range(0,len(tab["Resource"].keys())-1):
    if tab["Resource"][index].replace(" ","") == resource:
        importstr += f',\\ \n {tab["Endpoint"][index].replace(" ","")}Request,\\\n {tab["Endpoint"][index].replace(" ","")}Response'
    else:
        print(importstr)
        resource = tab["Resource"][index].replace(" ","")
        
        importstr = f'from API.Resources.{tab["Resource"][index].replace(" ","")} import {tab["Endpoint"][index].replace(" ","")}Request,\\\n {tab["Endpoint"][index].replace(" ","")}Response'

    0=1,2
    1=3,4
    2=5,6