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
  popu = (item["population"])
  native = (item["nativeName"])
  print("Pais:"+pais,"  Capital:"+capital,"  Region:"+region,"  Population: ",+popu, "  Native: "+native)

