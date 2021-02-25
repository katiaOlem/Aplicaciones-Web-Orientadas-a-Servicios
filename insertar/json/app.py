import json

class Json():
  json_file = {}

  def read(self):
    with open("datos.json") as file:
      self.json_file = json.load(file)
    print(self.json_file)
  
  def write(self):
    nombre = input ("Nombre: ")
    email = input ("Email: ")

    persona = {
      "nombre":nombre,
      "email":email
    }

    self.json_file["personas"].append(persona)
    with open ("datos.json","w") as  file :
      json.dumps(self.json_file,file)


objeto = Json()
objeto.read
objeto.write()
print(objeto.json_file)
