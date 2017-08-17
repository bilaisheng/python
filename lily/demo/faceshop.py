import lxml.html
import urllib.request
import csv


def download(url, free_proxy=None, user_agent='test', num_retries=2):
    print('download...')
    headers = {"User_agent" : user_agent}
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener()
    if free_proxy:
        proxy_params = {urllib.request.urlparse(url).scheme: free_proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib.request.URLError as e:
        print("download error",e.reason)
        html = None
        if num_retries> 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                html = download(url, free_proxy, user_agent, num_retries - 1)
    return html


def write_title(self):
    self.writer =csv.writer(open('faceshop.csv', 'w'))
    self.fields = ('id', 'Name', 'Address')
    self.writer.writerrow(self.fields)


def write_content(url):
    html = download(url)
    tree = lxml.html.fromstring(html)
    stores = tree.cssselect('div.store-content > table > tbody > tr')
    f = open('faceshop.csv', 'w', encoding='utf-8')
    f.write('id,Name,Address\n')
    for store in stores:
        store_info = store.cssselect('td')
        for store_info in store_info:
            print(store_info.text_content())
            f.write(str(store_info.text_content())+',')
        f.write('\n')
    f.close()

write_content('http://www.thefaceshop.com.cn/store-locations')

