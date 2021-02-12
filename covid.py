import json
import requests


result = requests.get("https://api.covid19api.com/total/dayone/country/china/status/confirmed")
print(result.status_code)
print(result.headers["Content-Type"])
result = result.json()
for item in result:
  fecha = str(item["Date"])
  pais = str(item["Country"])
  casos = (item["Cases"])
  status = (item["Status"])
  
  print("Pais:"+pais,"Fecha:"+fecha,"Country:"+pais,"Casos:"+casos,"Status:"+status)


