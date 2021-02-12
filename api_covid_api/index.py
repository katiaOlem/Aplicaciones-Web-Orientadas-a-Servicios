import web
import requests
import json

render=web.template.render("api_covid_api/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)
  def POST(self):
    form=web.input()
    nombre=form.nombre
    result = requests.get("https://api.covid19api.com/total/dayone/country/china/status/confirmed"+nombre)
    print(result.headers["Content-Type"])
    result = result.json()
    for item in result:
     
      casos = str(item["Cases"])
      status = str(item["Status"])
      fecha  = str(item["Date"])
  
      datos={
      "PAIS":"Pais:   "+nombre,
      "CASOS":"Casos:   "+casos,
      "STATUS":"status:    "+status,
      "FECHA":"fecha:   "+fecha
      
    }
      
    return render.index(datos)