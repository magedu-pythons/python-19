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
