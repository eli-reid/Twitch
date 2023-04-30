import requests
import pandas as pd

resp=requests.get("https://dev.twitch.tv/docs/api/reference/")

tables = pd.read_html(resp.content)

tab = tables[0].to_dict()
i = 1 
for index in range(0, len(tab.items())):
    requestparams = tables[i]
    respparams = tables[i+1]
    string = f'async def {tab["Endpoint"][index].replace(" ","")}(self,)'
    tab["Endpoint"][index].replace(" ","")
