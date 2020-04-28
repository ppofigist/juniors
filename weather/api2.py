import requests

print('Введите города через пробел')
city = input()
citys = ''.join(city).split(' ')
print(citys)
for elem in citys:
    zapros = 'http://wttr.in/' + elem + '?format=3'
    r = requests.get(zapros)
    print(r.text)

