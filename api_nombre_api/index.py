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
    response = response.json()
    for item in response:
      
      capital = (item["capital"])
      region = (item["region"])
      native = (item["nativeName"])
      flagi = (item["flag"])
      imagen = "<img src='"+flagi+"'/>"
 
    datos={
      "PAIS":"Pais:  "+nombre,
      "CAPITAL":"Capital:   "+capital,
      "REGION":"Region:    "+region,
      "NATIVE":"Native:   "+native,
      "FLAG":"Bandera:"   +imagen
    }
      
    return render.index(datos)