import urllib.parse
import urllib.request
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord', 'location' : 'Northampton', 'language' : 'Python' }
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req=urllib.request.Request(url,data)
response = urllib.request.urlopen(req)
the_page = response.read()
print(req)