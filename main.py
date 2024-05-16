import requests
result = requests.get('http://127.0.0.1:8000/api/task-list/')
result.json()

response = result.json()

print(response)

# for i in response:
#     print(i)