# 1、并发抓取10 个url，并且打印出它们的状态码、和文本内容
import requests
import threading
import logging

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

urls = ('https://news.sina.com.cn/',
        'https://mil.news.sina.com.cn/',
        'https://news.sina.com.cn/china/',
        'https://news.sina.com.cn/world/',
        'https://finance.sina.com.cn/stock/',
        'https://finance.sina.com.cn/fund/',
        'https://finance.sina.com.cn/forex/',
        'https://tech.sina.com.cn/',
        'https://mobile.sina.com.cn/',
        'https://www.sina.com.cn/'
        )


def get_all(urls):
    res = dict()
    for u in urls:
        threading.Thread(target=get_one, args=(u, res)).start()


def get_one(url, res):
    r = requests.get(url)
    res[r.text] = r.status_code
    logging.info('{}\n{}'.format(r.status_code, r.text))


# test
get_all(urls)


# 2、上下文管理是什么？请实现一个python 类，具有上下文管理功能
# 上下文管理:
# 在需要执行一个语句块或者实例化一个对象的时候, 有时会需要配置一些使用的资源,
# 并在结束时及时释放资源, 上下文管理就是控制代码执行前的准备以及执行后的收尾工作,
# 需要用with语法

class A:
    def __init__(self, name='tom'):
        print('init')
        self._name = name

    """
    进入与这个对象相关的上下文, 如果存在该方法, 
    with语句会把该方法的返回值作为绑定到as子句中指定的变量上;
    enter的返回值将作为as子句后面的变量的值
    """

    def __enter__(self):
        print('enter')
        return 'I am __exit__'

    # 退出与这个对象相关的上下文
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    @property
    def name(self):
        return self._name

    def __str__(self):
        return 'my name is {}'.format(self._name)


"""
#只有进入with语法时才开启上下文,但是是否支持上下文管理,还需要看有没有定义上述的两个特殊方法
#就算遇到了退出进程的错误(sys.exit),上下文也能完成完整的清理
"""
with A() as a:
    print(a)
