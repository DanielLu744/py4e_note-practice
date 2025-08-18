import urllib.request, urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

address = 'Erhvervsakademi Sydvest'
parms = {'q': address}

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

plus_code = js['features'][0]['properties']['plus_code']
print('Plus code', plus_code)
