from bs4 import BeautifulSoup

html_sample = '\
<html>\
<body>\
<h1 id="title">Hello World!</h1>\
<a href="#" class="link">This is link1</a>\
<a href="# link2" class="link">This is link1</a>\
</body>\
</html>'

# 如果不指明剖析器，会提示警告，但无影响，
# html.parser 增加后无警告
soup = BeautifulSoup(html_sample, 'html.parser')
print(soup.text)