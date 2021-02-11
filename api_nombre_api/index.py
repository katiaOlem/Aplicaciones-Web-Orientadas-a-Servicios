import web
import requests
import json
render=web.template.render("api_nombre_api/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)
  def POST(self):
    form=web.input()
    nombre=form.nombre
    result = requests.get("https://api.covid19api.com/total/dayone/country/china/status/confirmed"+nombre)
    cov = result.json()
    cov_coun = cov[0]
    cov_country = cov_coun["Country"]
    cov_country_date = cov_coun["Date"]
    cov_country_status = cov_coun["Status"]
    cov_country_cases = cov_coun["Cases"]
    datos={
      "country":"Country: "+cov_country,
      "dato":"Datos: "+cov_country_date,
      "status":"Status: "+cov_country_status,
      "cases":"Casos: "+cov_country_cases
      
    }
    return render.index(datos)