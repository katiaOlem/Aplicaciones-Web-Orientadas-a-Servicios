import json
import requests
import web

result = requests.get("https://api.covid19api.com/total/dayone/country/china/status/confirmed")
print(result.status_code)
print(result.headers["Content-type"])
cov = result.json()
cov_coun = cov[0]
cov_country = cov_coun["Country"]
cov_country_date = cov_coun["Date"]
cov_country_status = cov_coun["Status"]
cov_country_cases = cov_coun["Cases"]
print(cov_coun)
print(cov_country)
print(cov_country_date)
print(cov_country_status)
print(cov_country_cases)