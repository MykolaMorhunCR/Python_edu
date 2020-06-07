import requests

url = "https://dev.trainest.com/api/v1/admin-sessions"

payload = "{\r\n  \"email\": \"sergii.diachkov.cr@gmail.com\",\r\n  \"password\": \"Qwerty12\",\r\n  \"lifeTime\": 6000\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

