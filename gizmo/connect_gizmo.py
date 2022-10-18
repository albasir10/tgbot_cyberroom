import requests

login = "albert"
password = "admin"
print(requests.get("http://"+login+":"+password+"@127.0.0.1:80/api/reports/sale"))
response = requests.get("http://"+login+":"+password+"@127.0.0.1:80/api/reports/sale    ")
print(response.text)