#!/usr/bin/python3
# Filename : json-csv_3.py
# Author by : Lily
"""
版本三
将多条json写入csv,其中几条缺少了部分键值对
"""
json_data = [{"id":"216","city":"\u4e1c\u839e\u5e02","county":"\u5e02\u3001\u53bf\u7ea7\u5e02","detail":"\u4e1c\u839e\u5e02\u5858\u53a6\u9547\u4e07\u79d1\u751f\u6d3b\u5e7f\u573aB7\u3001B8\u53f7","time":"2015-09-23"},
             {"id":"72","province":"\u5e7f\u4e1c\u7701","city":"\u5e7f\u5dde\u5e02","detail":"\u5e7f\u5dde\u5e02\u9ec4\u57d4\u533a\u9ec4\u57d4\u4e1c\u8def2700\u53f7\u534e\u6da6\u4e07\u5bb6\u9996\u5c42","phone":"","time":"2015-08-03"},
             {"id":"376","city":"\u60e0\u5dde\u5e02","county":"\u60e0\u57ce\u533a","detail":"\u60e0\u6c34\u533a\u73af\u57ce\u897f\u4e8c\u8def33\u53f7","phone":"","time":"2016-09-22"},
             {"id":"51","province":"\u5e7f\u4e1c\u7701","city":"\u5e7f\u5dde\u5e02","county":"\u6d77\u73e0\u533a","detail":"\u5e7f\u5dde\u5e02\u6d77\u73e0\u533a\u58a9\u548c\u8def165\u53f7\u6566\u714c\u5546\u4e1a\u57ceA6\u6863","phone":"020-84217995","time":"2015-08-03"},
             {"id":"391","province":"\u6e56\u5317\u7701","county":"\u5e02\u3001\u53bf\u7ea7\u5e02","detail":"\u5929\u95e8\u5e02\u5f20\u6e2f\u9547\u666f\u5cf0\u5927\u9053","phone":"","time":"2016-09-26"}]


def muti_json(file_name,json_data):
    # 打开CSV
    f = open(file_name,'w',encoding='utf-8')
    # 定义tittle
    tittle = []
    # 遍历所有的键值对，取到所有不重复的键（做 title）
    for l in json_data:
        for k in l:
            if k not in tittle:
                tittle.append(k)
                print(k)
    # 把 tittle 写入表格
    for ti in tittle:
        f.write(ti)
        f.write(',')
    f.write('\n')

    # 初始化data(一条json)
    data = []
    for i in range(len(tittle)):
        data.append(' ')
    # 遍历每一个键值对，将值写入表格
    for l in json_data:
        # 按照title的顺序把value存到data
        for k, v in l.items():
            data[tittle.index(k)] = v
        # 将data写 入表格
        for da in data:
            f.write(da)
            f.write(',')
        f.write('\n')

muti_json('test3.csv',json_data)
