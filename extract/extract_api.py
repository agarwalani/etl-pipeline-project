import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()