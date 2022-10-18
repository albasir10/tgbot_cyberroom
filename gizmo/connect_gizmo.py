import requests

login = "albert"
password = "admin"
print(requests.get("http://"+login+":"+password+"@127.0.0.1:80/api/reservations"))
response = requests.get("http://"+login+":"+password+"@127.0.0.1:80/api/reservations")
print(response.text)