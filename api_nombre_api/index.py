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
    result = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=a89a7a3b"+nombre)
    api = result.json()
    titulo = api["Title"]
    anio = api["Year"]
    actores = api["Actors"]
    director = api["Director"]
    post = api["Poster"]
    tipo = api["Type"]

    datos={
      "titulopeli":"Country: "+titulo,
      "aniopeli":"Datos: "+anio,
      "actorespeli":"Status: "+actores,
      "postpeli":"Casos: "+post,
      "tipopeli":"Tipo: "+tipo,
      "directorpeli":"Director: "+director
    }
    return render.index(datos)