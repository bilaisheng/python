"""
Author:Lily
Date:2018-09-12
QQ:339600718
Capture Data: Communes of Cambodia
URL:https://en.wikipedia.org/wiki/Communes_of_Cambodia?tdsourcetag=s_pctim_aiomsg
"""
import requests
from lxml import etree

url = 'https://en.wikipedia.org/wiki/Communes_of_Cambodia?tdsourcetag=s_pctim_aiomsg'
html = requests.get(url)
print(html.text)



