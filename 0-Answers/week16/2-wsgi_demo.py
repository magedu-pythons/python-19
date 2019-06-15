# 2、实现一个wsgi的http web服务端

from pprint import pformat
from wsgiref.simple_server import make_server

def app(env, start_response):
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    start_response('200 OK', list(headers.items()))
    yield 'hello world: \r\n\r\n'.encode('utf-8')
    yield pformat(env).encode('utf-8')

if __name__ == '__main__':
    httpd = make_server('', 7000, app)
    host, port = httpd.socket.getsockname()
    print(host, port)
    httpd.serve_forever()
