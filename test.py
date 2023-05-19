import requests

BASE = "http://127.0.0.1:5000/"

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}
data = [
    {"name": "luna", "type": "dog", "race": "white swiss", "age": 2},
    {"name": "Jaskier", "type": "dog", "race": "Akita", "age": 4}
]
for i in range(len(data)):
    response = requests.post(BASE + "animal/" + str(i), json=data[i], headers=headers)
    print(response)
response = requests.get(BASE + "animal/0")
response2 = requests.get(BASE + "animals")
print(response.json())
print(response2.json())
# input()
