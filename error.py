import requests


try:
    data = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    print(data[1:4])


except Exception as error:
    print(error)
