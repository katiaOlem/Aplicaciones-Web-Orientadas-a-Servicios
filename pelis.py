import json
import requests
import web

result = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=a89a7a3b")
print(result.status_code)
print(result.headers["Content-Type"])
api = result.json()
titulo = api["Title"]
anio = api["Year"]
actores = api["Actors"]
director = api["Director"]
post = api["Poster"]
tipo = api["Type"]
print(titulo)
print(anio)
print(actores)
print(director)
print(post)
print(tipo)
