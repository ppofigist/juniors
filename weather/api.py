import requests

print('Введите город')
city = input()
while city != '':
    zapros = 'http://wttr.in/' + city + '?format=3'
    r = requests.get(zapros)
    print(r.text)
    city = input()
