import requests
import json


url = "https://restcountries.eu/rest/v2/all"
response = requests.get(url)
print(response.headers["Content-Type"])
response = response.json()
for item in response:
  pais = (item["name"])
  capital = (item["capital"])
  region = (item["region"])
  native = (item["nativeName"])
  flag = (item["flag"])
  print("Pais:"+pais,"  Capital:"+capital,"  Region:"+region, "  Native: "+native)

