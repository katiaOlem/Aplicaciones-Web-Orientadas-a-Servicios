import requests
import json

response = requests.get("https://restcountries.eu/rest/v2/name/")
print(response.headers["Content-Type"])
response = response.json()
for item in response:
  pais = (item["name"])
  capital = (item["capital"])
  region = (item["region"])
  native = (item["nativeName"])
  flag = (item["flag"])
  print("Pais:"+pais,"  Capital:"+capital,"  Region:"+region, "  Native: "+native)

