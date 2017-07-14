#!/usr/bin/python3
# Filename : json-csv_2.py
# Author by : Lily
"""
版本2
将多条json数据写入csv

"""

json_data = [{"id":"216","province":"\u5e7f\u4e1c\u7701","city":"\u4e1c\u839e\u5e02","county":"\u5e02\u3001\u53bf\u7ea7\u5e02","detail":"\u4e1c\u839e\u5e02\u5858\u53a6\u9547\u4e07\u79d1\u751f\u6d3b\u5e7f\u573aB7\u3001B8\u53f7","phone":"","time":"2015-09-23"},
             {"id":"72","province":"\u5e7f\u4e1c\u7701","city":"\u5e7f\u5dde\u5e02","county":"\u9ec4\u57d4\u533a","detail":"\u5e7f\u5dde\u5e02\u9ec4\u57d4\u533a\u9ec4\u57d4\u4e1c\u8def2700\u53f7\u534e\u6da6\u4e07\u5bb6\u9996\u5c42","phone":"","time":"2015-08-03"},
             {"id":"376","province":"\u5e7f\u4e1c\u7701","city":"\u60e0\u5dde\u5e02","county":"\u60e0\u57ce\u533a","detail":"\u60e0\u6c34\u533a\u73af\u57ce\u897f\u4e8c\u8def33\u53f7","phone":"","time":"2016-09-22"},
             {"id":"51","province":"\u5e7f\u4e1c\u7701","city":"\u5e7f\u5dde\u5e02","county":"\u6d77\u73e0\u533a","detail":"\u5e7f\u5dde\u5e02\u6d77\u73e0\u533a\u58a9\u548c\u8def165\u53f7\u6566\u714c\u5546\u4e1a\u57ceA6\u6863","phone":"020-84217995","time":"2015-08-03"},
             {"id":"391","province":"\u6e56\u5317\u7701","city": "\u5730\u7ea7\u5e02","county":"\u5e02\u3001\u53bf\u7ea7\u5e02","detail":"\u5929\u95e8\u5e02\u5f20\u6e2f\u9547\u666f\u5cf0\u5927\u9053","phone":"","time":"2016-09-26"}]

f = open('test2.csv','w',encoding='utf-8')


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
for j in json_data:
        write_tittle(j)
        break
for j in json_data:
        write_data(j)