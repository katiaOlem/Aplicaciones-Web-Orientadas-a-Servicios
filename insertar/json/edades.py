import web
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:

    json_file = {}


    def GET(self):

        parametros = web.input()
        action = parametros.action

        if action == "get":
            return self.read()
        elif action == "put":
            nombre = parametros.nombre
            fecha_naci = parametros.fecha_naci
            return self.write(nombre, fecha_naci)
        else:
            datos = {}
            datos["result"] = "**Error**"
            return json.dumps(datos)

    def write (self, nombre,fecha_naci):
      try:
        fecha_nacimiento = datetime.strptime(fecha_naci, "%d-%m-%Y") #//fecha
        edad = relativedelta(datetime.now(), fecha_nacimiento) #Almacene valores en edad
        edad = (f"{edad.years} years.")
        datos = {
        "nombre" : nombre,
        "fecha_naci" : fecha_naci,
        "edad" : edad
        }
        try:
          with open("datos.json") as file:
            self.json_file = json.load(file)
            self.json_file["datos"].append(datos)
            with open("datos.json","w") as file:
              json.dump(self.json_file, file)
              return json.dumps(datos)

        except  Exception as error:
          print("Error {}".format(error.args[0]))
          return json.dumps(datos)
            
      except  Exception as error:
        print("Error {}".format(error.args[0]))
        return json.dumps(datos)
    
    def read(self):
      try:
        with open("datos.json") as file:
            self.json_file = json.load(file)
            print(self.json_file)
            return json.dumps(self.json_file)

      except Exception as error:
        print("Error {}".format(error.args[0]))




if __name__ == "__main__":
    app.run()