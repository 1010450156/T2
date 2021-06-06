#-*- coding: utf-8 -*-
#@File      :PostAndGet.py
#@Time      :2021/6/5 19:29
#@Author    :xiaona
#@Software  :PyCharm

import requests
import json


class Testrequests():
    def get(self,url,data,headers):
        try:
            r = requests.get(url,params=data,headers=headers)
            r.encoding = 'utf-8'
            json_r = r.json()
            print("Test执行结果：",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))
    def post(self,url,data,headers):
        try:
            r = requests.post(url,data=data,headers=headers)
            r.encoding = 'utf-8'
            json_r = r.json()
            print("Test执行结果：",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))

    def run_main(self, method,url,data,headers):
        result = None
        if method == 'post':
            result = self.post(url,data=data,headers=headers)
        elif method == 'get':
            result = self.get(url,data=data,headers=headers)
        else:
            print("method值错误！！！")
        return result

if __name__ == '__main__':
    Testrequests().run_main('post','http://121.41.14.39:8082/account/sLogin',{"username": "dp0426", "password": "131eb75ea610671aad36a40496850d58"},None)