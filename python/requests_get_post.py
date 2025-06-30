import requests

response  = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data)

for post in data:
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}\n")    


url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
#response = requests.post(url, json=payload)
#print(response.json())

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET Status Code:", response.status_code)
print("GET Data:", response.json())

# Post request
new_post = {
    'title': 'AI Learning',
    'body': 'Exploring the world of Artificial Intelligence.',
    'userId': 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print("POST Status Code:", response.status_code)
print("POST Response:", response.json())