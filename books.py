import requests
import json


result = requests.get("https://www.googleapis.com/books/v1/volumes?q=harry")
print(result.status_code)
print(result.headers["Content-Type"])
books = result.json()
print(books["totalItems"])
items = books["items"]
print(items[0].keys())
encode = json.dumps(items)
decode = json.loads(encode)
print(decode[0]["volumeInfo"]["title"])