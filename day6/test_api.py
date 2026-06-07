import requests

def test_api():
    # GET Request
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # Status Code
    print(response.status_code)

    # Response Header
    print(response.headers['Content-Type'])

    # Response Body as JSON
    data = response.json()
    print(data)

    # Response time
    print(response.elapsed.total_seconds())
