import web
import requests
import json
render=web.template.render("api_nombre_api/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)
  def POST(self):
    form=web.input()
    nombre=form.nombre
    url = "https://restcountries.eu/rest/v2/all"
    response = requests.get(url)
    print(response.headers["Content-Type"])
    response = response.json()
    for item in response:
      
      capital = (item["capital"])
      region = (item["region"])
      popu = (item["population"])
      native = (item["nativeName"])
 
    datos={
      "PAIS":"Pais"+nombre,
      "CAPITAL":"Capital:"+capital,
      "REGION":"Region:"+region,
      "POPULATION":"Sub-Region:"+popu,
      "NATIVE":"Native: "+native
    }
      
    return render.index(datos)