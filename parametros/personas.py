import web
import json
urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:

    def GET(self,fecha_naci):
        try:
            parametros = web.input()
            nombre = parametros.nombre
            day = int(parametros.day)
            month = int(parametros.month)
            year = int(parametros.year)
            edad = 2021 - year
            edad = day - 1
            edad = month -1

            dato = {}
            dato["nombre"] = nombre
            dato["day"] = day
            dato["month"] = month
            dato["year"] = year
            dato["edad"] = edad
            dato["status"] = 200
            archivo = open("static/datos.txt","a")
            archivo.write("\nNombre: "+dato["nombre"]+"\n")
            archivo.write("Fecha de nacimiento: "+dato["day"]+dato["month"]+dato["year"]+".\n")
            archivo.write("Edad: "+dato["edad"]+"\n")
            archivo.close()
            return json.dumps(dato)
            
        except:
            dato = {}
            dato["status"] = "Verifica datos. Error 404 not found"
            return json.dumps(dato)

if __name__ == "__main__":
  app.run()