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
response = requests.post(url, json=payload)
print(response.json())