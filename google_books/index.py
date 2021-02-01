import web
import requests
import json
render=web.template.render("google_books/")

class Index():
  def GET(self):
    libros=None
    return render.index(libros)
  def POST(self):
    form=web.input()
    book_name=form.book_name
    result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)
    book = result.json()
    items = book["items"]
    encoded = json.dumps(items)
    decoded = json.loads(encoded)
    nombre_autor=str(decoded[0]["volumeInfo"]["authors"])
    url_imagen=decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"]
    url = decoded[0]["volumeInfo"]["infoLink"]
    imagen ="<img src='"+url_imagen+"'/>"
    autor="<label>'"+nombre_autor+"'</label>"
    link ="<a target='blank' href='"+url+"'>"+book_name+"</a>"
    
    
    libros={
      "imagen":imagen,
      "nombre_libro":"Libro  "+book_name,
      "autor":"Autor  "+autor,
      "url":"Compra  "+link
    }
    return render.index(libros)