# 18周作业
# 1、实现一个socket服务端和客户端，客户端发送消息给服务端，服务端返回客户端ip+port 带上收到的消息返回 给客户端，支持客户端发送 'quit'消息，主动断开连接。
# server
import socket
import threading


class Server:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        print('start')
        self.sock.bind(self.addr)
        self.sock.listen()

        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            newsock, raddr = self.sock.accept()

            threading.Thread(target=self.recv, name='recv', args=(newsock, raddr)).start()

    def recv(self, newsock, raddr):
        while not self.event.is_set():
            try:
                data = newsock.recv(1024)
            except Exception as e:
                data = b'quit'
            if data == b'quit':
                newsock.close()
                break
            msg = 'ip:{} port{} message:{}'.format(*raddr, data.decode()).encode()
            newsock.send(msg)

    def stop(self):
        print('stop')
        self.sock.close()
        self.event.set()



def main():
    s = Server()
    s.start()
    while True:
        cmd = input('cmd>>>>>')
        if cmd.strip() == 'quit':
            s.stop()
            threading.Event.wait(3)
            break


if __name__ == '__main__':
    main()


# client
import socket
import threading


class Client:
    def __init__(self, rip='127.0.0.1', rport=9999):
        self.raddr = (rip, rport)
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.raddr)

        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)
            except Exception as e:
                pass
            else:
                print(data)

    def send(self, msg):
        if msg == 'quit':
            self.event.set()
            self.stop()
            return 0
        self.sock.send(msg.encode())

    def stop(self):
        self.sock.close()
        self.event.set()


def main():
    c = Client()
    c.start()
    while True:
        cmd = input('message:')
        c.send(cmd)


if __name__ == '__main__':
    main()


# 2、实现一个wsgi的http web服务端
# 这块内容还没有学好，等学好了来补上
from wsgiref.simple_server import make_server


def simple_app(environ, start_response):  # 这两个参数是自动注入的
    # print(environ)
    for k, v in sorted(environ.items()):
        print(k, v)
    print('-' * 30)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)  # 在返回正文之前首先要返回状态码,报文头

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret  # 这里return的是正文,必须是个可迭代对象,一般是列表,可以是一个字符串元素


# 关于APP的其他写法A:
class simple_app_A():
    def __init__(self, name, age):
        pass

    def __call__(self, environ, start_response):
        pass


# 关于APP的其他写法B:
class simple_app_B():
    def __init__(self, environ, start_response):
        for k, v in sorted(environ.items()):
            print(k, v)
        print('-' * 30)
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        self.ret = [("%s: %s\n" % (key, value)).encode("utf-8")
                    for key, value in environ.items()]

    def __iter__(self):
        yield from self.ret


# make_server('0.0.0.0', 9000, simple_app_A('tom', 20))
# make_server('0.0.0.0', 9000, simple_app_B)
with make_server('0.0.0.0', 9000, simple_app) as httpd:  # 撞见server
    print("Serving on port 9000...")
    httpd.serve_forever()
