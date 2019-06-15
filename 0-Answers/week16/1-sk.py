# 1、实现一个socket服务端和客户端，客户端发送消息给服务端，
# 服务端返回客户端ip+port 带上收到的消息返回 给客户端，支持客户端发送 'quit'消息，主动断开连接。

import socket


def my_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_hostname = socket.gethostname()
    ip_address = socket.gethostbyname(local_hostname)
    server_address = (ip_address, 5050)
    s.bind(server_address)
    s.listen(1)
    while True:
        connection, client_address = s.accept()
        try:
            print('connection from', client_address)
            # receive the data in small chunks and print it
            while True:
                data = connection.recv(1024)
                if data:
                    # output received data
                    print("Data: %s" % data)
                    resp = '{} {} {}'.format(data, *client_address)
                    connection.send(resp.encode())
                if data.decode() == 'quit':
                    # no more data -- quit the loop
                    print("no more data.")
                    break
        finally:
            # Clean up the connection
            connection.close()


def my_client(ip, port, msg):
    c = socket.socket()
    c.connect((ip, port))
    c.send(msg.encode())
    resp = c.recv(1024)
    print(resp)