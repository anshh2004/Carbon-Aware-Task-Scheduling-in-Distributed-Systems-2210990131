import requests

url = "https://api2.watttime.org/v2/register"

data = {
    "username": "ansh123",
    "password": "Ansh@123",
    "email": "bansalansh0024@gmail.com",
    "org": "Student Project"
}

response = requests.post(url, json=data)

print(response.text)