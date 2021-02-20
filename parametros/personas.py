import web
import json
import datetime 

urls = {
  "/datos?","Personas"
}

app = web.application(urls,globals())

class Personas(naci):
  def GET(self):
    try:
      personas.web.input()
      nombre = personas.nombre
      hoy = datetime.date.today()
      
      if hoy < naci:
        'error en la fecha de nacimiento'
      else:
        anio = naci.year
        mes = naci.month
        dia = naci.day
        fecha = naci
        edad = 0
       
      while fecha < hoy:
        edad += 1
        fecha = datetime.date(anio+edad, mes, dia)
        data = {}
        data["nombre"] = nombre
        data["anio"] = anio
        data["mes"] = mes
        data["dia"] = dia
        data["edad"] = edad
        data["fecha"] = fecha
       
       archivo = open("static/datos.txt","a")
       archivo.write("\nNombre: "+data["nombre"]+"\n")
       archivo.write("Fecha de nacimiento: "+data["fecha"]+".\n")
       archivo.write("Edad: "+data["edad"]+"\n")
       archivo.close()
       return json.dumps(data)

    except:
      data = {}
      data["error"] = "Datos Incorrectos!**Verifique sus datos."
      data["status"] = 404
      return json.dumps(data)


if __name__ == "__main__":
    app.run()