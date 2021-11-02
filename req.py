import requests
import json
url = "https://api.countrystatecity.in/v1/countries"

headers = {
  'X-CSCAPI-KEY': 'Tmk5Y3ZJQ0RRM1dWUmZHUFlDbGU1Y0o1ZjlXRkcwendEUHlLT1VNcg=='
}

response = requests.request("GET", url, headers=headers)

data = response.json()

# countries = [country['name'] for country in data]
# print(countries)

# dict_countries = {x['iso2']:x['name'] for x in data}
# print(dict_countries)

dict_countries = {x['name']:x['iso2'] for x in data}
print(dict_countries)

dict_countries = {x['name']: x['iso2'] for x in data}        
urlp = f"""https://api.countrystatecity.in/v1/countries/AF/states"""

headers1 = {
            'X-CSCAPI-KEY': 'Tmk5Y3ZJQ0RRM1dWUmZHUFlDbGU1Y0o1ZjlXRkcwendEUHlLT1VNcg=='
          }

response = requests.request("GET", urlp, headers=headers1)
data = response.json()
states = [x['name'] for x in data]
print(states)
