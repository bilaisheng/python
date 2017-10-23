import requests
import pprint

url = "https://www.mcdonalds.com.cn/ajaxs/search_by_point"

headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate,br'
}

response = requests.post(url, data={'point': '113.301193570281,23.113900522523'}, verify=False)

print(response.text)
