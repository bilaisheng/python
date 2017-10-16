from bs4 import BeautifulSoup

html_sample = '\
<html>\
<body>\
<h1 id="title">Hello World!</h1>\
<a href="#" class="link">This is link1</a>\
<a href="# link2" class="link1">This is link2</a>\
</body>\
</html>'

# 如果不指明剖析器，会提示警告，但无影响，
# html.parser 增加后无警告
soup = BeautifulSoup(html_sample, 'html.parser')
print(soup.text)

header = soup.select('h1')
print(header)
print(header[0])
print(header[0].text)

pid = soup.select('#title')
print(pid)

alink = soup.select('a')
print(alink)
for link in alink:
    print(link)
    print(link.text)
    print(link['href'])

for link in soup.select('.link'):
    print(link)