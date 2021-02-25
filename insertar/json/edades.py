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
            edad = (f"{edad.years} años.")
            datosper = {}
            datosper["nombre"] = nombre
            datosper["fecha_nacimiento"] = fecha_naci
            datosper["edad"] = edad
            
            try:
                with open("datos.json") as file:
                    self.json_file = json.load(file)
                    self.json_file["datos"].append(datosper)
                    with open("datos.json","w") as file:
                        json.dumps(self.json_file, file)
                        datos = {}
                        return json.dumps(datos)
            except:
                datos = {}
                datos["error"] = "***Error****"
                return json.dumps(datos)
            
        except:
            datos = {}
            datos["error"] = "*****Error****"
        
            return json.dumps(datos)
    
    def read(self):
        with open("datos.json") as file:
            self.json_file = json.load(file)
            return json.dumps(self.json_file)




if __name__ == "__main__":
    app.run()