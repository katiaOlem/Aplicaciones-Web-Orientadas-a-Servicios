import json


class Parametros():
  json_file={}

  def read(self):
      with open("datos.json") as file:
        self.json_file = json.load(file)
      print(self.jason_file)

    
objeto= Parametros()
objeto.read()