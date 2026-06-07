import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
user = response.json()

# Access top level fields
print(user['name'])
print(user['email'])
print(user['phone'])

# Access the nested fields
print(user['address']['city'])
print(user['address']['geo']['lat'])

## Assertions

assert response.status_code == 200, \
    f'Expected 200, got {response.status_code}'

assert 'application/json' in response.headers['content-type'], \
    f'Expected json, got {response.headers['content-type']}'

assert 'id' in user, 'Response missing id'
assert 'email' in user, 'Response missing email'

assert user['id'] == 1, f'ID should be 1'


