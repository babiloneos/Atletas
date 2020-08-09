import requests

url = "http://localhost:5000/login"

username = "admin"
password= "121176"

payload = {'username': username, 'password': password}

r = requests.post(url, data = payload)

print(r.text)
