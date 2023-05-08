import requests
import pandas as pd
file = open("fields.py","w+")
fieldtype = {"String":"str",
             "Boolean":"bool",
             "Integer":"int",
             "Dictionary":"dict",
             "String[]":"list[str]",
             "Object[]":"list[object]",
             "Object":"object"
}
resp=requests.get("https://dev.twitch.tv/docs/api/reference/")

tables = pd.read_html(resp.content)
tabs:list[dict] = []

for table in tables:
    tabs.append(table.to_dict())
i = 0 
for tab in tabs:
    if tab.get("Code") or tab.get("HTTP Code") : 
        index = tabs.index(tab)-1
        tmptab=tabs[index]
        if tmptab.get("Field") is not None:
            for key in tmptab["Field"].keys():
                if tmptab["Field"].get(key) == "data":
                    file.write(f"\n\nItem_Index : {i}\n")
                    file.write(f"{tabs[0].get('Endpoint').get(i)}\n")
                file.write(f'{tmptab["Field"].get(key)}: {fieldtype.get(tmptab["Type"].get(key)) } \n ')
        i+=1
file.close()
