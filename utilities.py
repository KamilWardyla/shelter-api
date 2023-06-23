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
response3 = requests.delete(BASE + "animal/1", headers=headers)
data1 = {
    'name': 'Zaktualizowana Nazwa'
}
response2 = requests.get(BASE + "animals")
response4 = requests.patch(BASE + 'animal/1', json=data1, headers=headers)
print(f"Delete: {response3}")
print(f"Get index 0{response.json()}")
print(f"Patch: {response4.json()}")
print(f"Get animals: {response2.json()}")
input()
