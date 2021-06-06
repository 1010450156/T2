#-*- coding: utf-8 -*-
#@File      :TestJson.py
#@Time      :2021/6/6 20:16
#@Author    :xiaona
#@Software  :PyCharm

import json

def TestJson(json1,json2):
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)

    for src_list, dst_list in zip(sorted(dict1), sorted(dict2)):
        result = ""
        if str(dict1[src_list]) != str(dict2[dst_list]):
            result = "不相等!"
            print(src_list, dict1[src_list], dst_list, dict2[dst_list])
            return result
        else:
            result = "相等!"
            print(src_list, dict1[src_list], dst_list, dict2[dst_list])
            return result

if __name__ == '__main__':
    json1 = {"a":1,"b":2}
    json2 = {"a":3,"b":2}
    print("对比结果是：",TestJson(json.dumps(json1),json.dumps(json2)))