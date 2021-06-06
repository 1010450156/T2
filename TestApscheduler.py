#-*- coding: utf-8 -*-
#@File      :TestApscheduler.py
#@Time      :2021/6/6 17:48
#@Author    :xiaona
#@Software  :PyCharm

import time
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

def testBaidu(text):
    url = 'https://www.baidu.com'  # 路径
    print("执行结果：",requests.post(url, data=None))
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# 每隔 5分钟 运行一次
scheduler.add_job(testBaidu, 'interval', minutes=5, args=['job1'])
scheduler.start()

