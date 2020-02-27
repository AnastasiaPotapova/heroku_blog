import requests

a = requests.get("https://nast-blog.herokuapp.com/api/login/Masha/a")
print(a.content)