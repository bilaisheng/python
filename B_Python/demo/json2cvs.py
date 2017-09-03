import json
import csv

json_str = '[{"a":1,"b":"2","c":"3"},{"a":21,"c":"23","d":{"d1":"24"},"e":"25"}]'

o = json.loads(json_str)

def loop_data(o, k=''):
    global json_ob, c_line
    if isinstance(o, dict):
        for key, value in o.items():
            if (k == ''):
                loop_data(value, key)
            else:
                loop_data(value, k + '.' + key)
    elif isinstance(o, list):
        for ov in o:
            loop_data(ov, k)
    else:
        if k not in json_ob:
            json_ob[k] = {}
        json_ob[k][c_line] = o


def get_title_rows(json_ob):
    title = []
    row_num = 0
    rows = []
    for key in json_ob:
        title.append(key)
        v = json_ob[key]

        if len(v) > row_num:
            row_num = len(v)
        continue
    for i in range(row_num):
        row = {}
        for k in json_ob:
            v = json_ob[k]
            if i in v.keys():
                # 若有数据 ,则用填入表格
                row[k] = v[i]
            else:
                # 若没有数据 ,则用空补位
                row[k] = ''
        rows.append(row)
    return title, rows

def write_csv(title, rows, csv_file_name):
    # 输出文件名称  newline: 去掉csv中默认会写入空行的问题
    with open(csv_file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=title)
        writer.writeheader()
        writer.writerows(rows)

def json_to_csv(object_list):
    global json_ob, c_line
    json_ob = {}
    c_line = 0
    for ov in object_list:
        loop_data(ov)
        c_line += 1
    title, rows = get_title_rows(json_ob)
    write_csv(title, rows, 'test.csv')


json_to_csv(o)

