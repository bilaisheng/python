#!/usr/bin/python3
# Filename : json-csv_1.py
# Author by : Lily
"""
版本一
将规范的一条json数据写入csv
"""

json_data = {"name":"\u6d4e\u5357\u9ea6\u5f53\u52b3\u6d4e\u5357\u5c71\u5927\u8def\u9910\u5385","address":"\u6d4e\u5357\u5386\u57ce\u533a\u5c71\u5927\u8def146\u53f7\u6210\u5927\u9ad8\u79d1\u5e02\u573a\u4e00\u5c42","province":"\u5c71\u4e1c\u7701","city":"\u6d4e\u5357\u5e02","phone_number":"0531-88368548","type":[1,3,8]}

f = open('test.csv','w',encoding='utf-8')


def write_tittle (json_da):
    tittle =[]
    for k, v in json_da.items():
        tittle.append(k)
    for t in tittle:
        f.write('%s ,' %t)
    f.write('\n')


def write_data(json_da):
    data = []
    for k,v in json_da.items():
        data.append(v)
    for d in data:
        f.write('%s,'%d)
    f.write('\n')

write_tittle(json_data)
write_data(json_data)




