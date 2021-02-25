import json

class Json():
  json_file = {}
  def read(self):
    with open("datos.json") as file:
      self.json_file = json.load(file)
    print(self.json_file)
  


objeto = Json()
objeto.read()

