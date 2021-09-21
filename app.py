import requests
import json
import base64

url = 'http://localhost/wp/wp-json/wp/v2'

user = 'xyz'
password = 'zzzz'
creds = user + ':' + password

token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {
'date': '2021-09-21T01:00:00',
'title': 'First Test Post',
'content': 'This is our first post description',
'status': 'publish'
}

r = requests.post(url + '/posts', headers=header, json=post)
print(r)