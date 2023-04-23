file1 = open("list.txt","r")
newlines = []
lines = file1.readlines()
file2 = open("genapifunc.py","a+")
for line in lines:
    if len(line) == 0:
        continue
    nl=line.replace("<dd><a href=","").replace("</a></dd>","").replace(" ","").rstrip('\r\n') 
    if nl.find(">") == -1:
        continue
    funcName=nl[nl.find(">")+1:]
    defline = f'''    async def {funcName}(self) -> {funcName}Response:
        request = {funcName}Request()
        response = {funcName}Response()
        await self._twitchAPICall(request, response)
        return response
    ''' 
    file2.write(defline)
    file2.write("\r\n")
