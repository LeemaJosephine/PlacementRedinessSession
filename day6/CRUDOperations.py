import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# GET
response = requests.get(f'{BASE_URL}/posts')
print(f'Total posts: {len(response.json())}')

# GET - Fetch single post with query param
response = requests.get(f'{BASE_URL}/posts',params={'userId':1})
print(f'Posts by user 1: {len(response.json())}')

# POST - Create a new post
new_post ={
    "title": "API Post Title",
    "body": "Post Body",
    "userId": 1
}

response = requests.post(f'{BASE_URL}/posts',json=new_post)
print(response.json())
print(response.status_code)

# PUT - Full update

updated_pose ={
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}

response = requests.put(f'{BASE_URL}/posts/1',json=updated_pose)
print(response.json())
print(response.status_code)

# PATCH - Partial update
response = requests.patch(f'{BASE_URL}/posts/1', json={'title':'Patched Title'})
print(response.json())
print(response.status_code)

# Delete - Remove the resource
response = requests.delete(f'{BASE_URL}/posts/1')
print(response.json())
print(response.status_code)