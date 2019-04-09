import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/comments_164716.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
url = serviceurl + urllib.parse.urlencode(parms)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

total = 0
totalcount = 0

for count in counts :
    newnumber = count.text
    total = total + int(newnumber)
    totalcount = totalcount + 1

print('Count:',totalcount)
print('Sum:',total)
