import web
import json
urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():

  json_file={}

  def GET(self):
      parametros = web.input() 
      name = parametros.name
      day = int(parametros.day)
      month = parametros.month
      year = int(parametros.year)
      age = 2021 - year
              
      action = parametros["action"]

      if action == "put":
        return self.read()

      elif action == "get":
        return self.write(name, day, month, year,age)
      datos = {}
      datos["action"] = action
      return json.dumps(datos)
       

  def read(self):
    try:
      with open("datos.json") as file:
        self.json_file = json.load(file)
      print(self.jason_file)

    except Exception as error:
      print("Error {}".format(error.args[0]))

  def write(self, name, day, month, year, age):
    datos={
    "name" : name,
    "day" : day,
    "month" : month,
    "year" : year,
    "age" : age
    }
    self.json_file["personas"].append(datos)
    with open("datos.json","w") as file:
      json.dump(self.json_file, file)
 


   

if __name__ == "__main__":
  app.run()


