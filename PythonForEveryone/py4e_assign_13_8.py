import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_164717.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

for count in info['comments']:
    try:
        sum = count['count'] + sum
    except:
        sum = count['count']

print (sum)

import re
sentence = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+?@\S+", sentence)
print(y)