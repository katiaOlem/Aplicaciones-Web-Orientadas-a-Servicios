import requests
import json
result=requests.get("https://www.googleapis.com/books/v1/volumes?q=harry+potter")
print(result.status_code)