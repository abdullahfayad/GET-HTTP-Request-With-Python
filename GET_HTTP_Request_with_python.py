import requests

r = requests.get('https://s-m.com.sa/', timeout=0.5)

print(r.content)
print(r.status_code)
print(r.headers)

