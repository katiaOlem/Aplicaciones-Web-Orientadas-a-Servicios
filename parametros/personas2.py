import web
import json
from datetime import datetime # //fecha actual
from dateutil.relativedelta import relativedelta #

urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:
    def __init__(self):
      pass
    
    def GET(self):
        try:
            parametros = web.input()
            nombre = parametros.nombre
            fecha_naci = parametros.fecha_naci

            fecha_nacimiento = datetime.strptime(fecha_naci, "%d-%m-%Y") #//fecha
            edad = relativedelta(datetime.now(), fecha_nacimiento) #Almacene valores en edad
            edad = (f"{edad.years} años.")
            datos = {}
            datos["status"] = 200
            datos["nombre"] = nombre
            datos["fecha_nacimiento"] = fecha_naci
            datos["edad"] = edad

            archivo = open("static/datos.txt","a")
            archivo.write("\n")
            archivo.write(str(datos))
            archivo.close()
            return json.dumps(datos)

            
          
           
           
            return json.dumps(datos)
            
        except:
            datos = {}
            datos["error"] = "Error*** Por favor verifique sus datos"
            datos["status"] = 404
            return json.dumps(datos)

if __name__ == "__main__":
    app.run()