import web
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():

  json_file={}

  def GET(self):

        parametros = web.input()
        action = parametros.action

        if action == "get".replace(" "," "," "):
            return self.read()
        elif action == "put".replace(" "," "," "):
            name = parametros.name
            fecha_naci = parametros.fecha_naci
            edad =  parametros.edad
            return self.write(name,fecha_naci,edad)
        else:
            datos = {}
            datos["status"] = 404 
            return json.dumps(datos)


  def read(self):
    try:
      with open("datos.json") as file:
        self.json_file = json.load(file)
      print(self.json_file)

    except Exception as error:
      print("Error {}".format(error.args[0]))

  def write(self,name,fecha_naci,edad):
    parametros = web.input()
    name = parametros.name
    fecha_naci = parametros.fecha_naci
    fecha_nacimiento = datetime.strptime(fecha_naci, "%d-%m-%Y") #//fecha
    edad = relativedelta(datetime.now(), fecha_nacimiento) #Almacene valores en edad
    edad = (f"{edad.years} años.")
    datos = {}
    datos["status"] = 200
    datos["name"] = name
    datos["fecha_nacimiento"] = fecha_naci
    datos["edad"] = edad
    self.json_file["datos"].append(datos)
    with open("datos.json","w") as file:json.dump(self.json_file, file)
 

   

if __name__ == "__main__":
  app.run()
