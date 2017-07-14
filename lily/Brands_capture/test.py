import json

data = [{"author": "作者", "parentTitle": "父标题", "title": "标题", "pageUrl": "pageurl", "link": "linkurl", "parentLink": "parenturl"}]

import codecs
file_object = codecs.open('tencent.csv', 'w' ,"utf-8")
str = "\r\n"
splitstr = "#_#"
for item in data:
    #print json.dumps(item)
    #str = str + "insert into tencent(name,catalog,workLocation,recruitNumber,detailLink,publishTime) values "
    #str = str + "'%s','%s','%s','%s','%s'\r\n" % (item['parentTitle'],item['parentLink'],item['author'],item['link'],item['title'])
    #print json.loads(item['author']) + "\r\n"
    str = "%s,%s,%s,%s,%s\r\n" % (item[data.keys()[0]],item['parentLink'],item['author'],item['link'],item['title'].strip())
    file_object.write(str)


file_object.close()
print("success")
