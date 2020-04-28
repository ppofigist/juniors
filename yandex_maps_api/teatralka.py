import requests

params = {'ll': '49.666698,58.603565',
          'size': '650,450',
          'l': 'sat',
          'z': '17'
          }
url = 'https://static-maps.yandex.ru/1.x'
r = requests.get(url, params=params)

f = open('title1.jpg', mode='wb')
f.write(r.content)
f.close()