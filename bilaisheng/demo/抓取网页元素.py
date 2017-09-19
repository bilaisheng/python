import urllib.request

from bs4 import BeautifulSoup

#沃尔玛
url = "http://www.wal-martchina.com/walmart/store/14_hubei.htm"

user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"

request = urllib.request.Request(url)

request.add_header("User-Agent", user_agent)

content = urllib.request.urlopen(request)

soup = BeautifulSoup(content,from_encoding="gb18030")

#店名
shopname = soup.find_all('td', {"class": "xl714445"})
#地址
addresss = soup.find_all('td', {"class": "xl684445"})
#联系电话
phones = soup.find_all('td', {"class": "xl744445"})

for shop in shopname:
    print("店铺名称:"+shop.text.lstrip().rstrip())

print("----------------------------------------------")

for address in addresss:
      print("店铺地址:"+address.text.lstrip().rstrip())

sum = 0
for phone in phones:
    if sum % 2 == 0:
        print("联系电话：" + phone.text.lstrip().rstrip())
    else:
        print("交通路线：" + phone.text.lstrip().rstrip())
        print('---------------------------------------------------')
    sum += 1
