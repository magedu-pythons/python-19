# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:23:03 2018

@author: guokang
"""

import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_one_page(url):
    try:
        headers = {
            'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'           
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' +
        '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' +
        '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
             'index': item[0],
             'image': item[1],
             'title': item[2],
             'actor': item[3].strip()[3:],
             'time':  item[4].strip()[5:],
             'score': item[5] + item[6]
        }
        
def write_to_file(content):
    with open('dianying.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii='False') + '\n')

print('开始爬取猫眼电影排行榜......')
time.sleep(5)
        
#整合代码
def main(offset):
    url = 'https://maoyan.com/board/4' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

#main(10)
#
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(2)
        
print('爬取首页完毕，并保存至dianying.txt中')   
            