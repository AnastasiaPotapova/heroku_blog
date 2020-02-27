import requests

a = requests.get("https://nast-blog.herokuapp.com/api/login/Nastya-potapova/a")
print(a.content)