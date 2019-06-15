import requests
import threading


# 1、并发抓取10 个url，并且打印出它们的状态码、和文本内容

def fetch(urls: list):
    def req(url):
        ret = requests.get(url)
        print(ret.status_code, ret.text)

    for l in urls:
        threading.Thread(target=req, args=(l,))
