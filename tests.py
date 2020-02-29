import requests

a = requests.post("https://nast-blog.herokuapp.com/api/post/1/test")
print(a.content)