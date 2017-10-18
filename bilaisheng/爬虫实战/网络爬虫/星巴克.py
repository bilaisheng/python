import requests
import pprint

url = "https://openapi.starbucks.com/v1/stores/nearby?limit=10&radius=10&latlng=22.54242,114.10799&access_token=28jhmjhe4dsr4n6nrj3xrxcv&locale=zh&callback=jQuery191038597660397573086_1508319944359&_=1508319944360"

headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate,br'
}

response = requests.get(url,verify=False)

result = str(response.text)

print(result[42:len(result)-1])
