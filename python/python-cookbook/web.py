from urllib import request, parse
import requests
from socketserver import BaseRequestHandler, StreamRequestHandler, ThreadingTCPServer, TCPServer, UDPServer
#from socket import socket, AF_INET, SOCK_STREAM
import time
import ssl
import multiprocessing

#13  发送和接受大型数组  memoryviews
def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]
    def recv_into(arr, source):
        view = memoryview(arr).cast('B')
        while len(view):
            nrecv = source.recv_into(view)
            view = view[nrecv:]

# test
#server
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
c,a = s.accept()
import numpy
a = numpy.arange(0.0, 50000000.0)
send_from(a, c)

#client
from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 25000))
import numpy
a = numpy.zeros(shape=50000000, dtype=float)
a[0:10]
recv_into(a, c)
a[0:10]

#12  理解事件驱动的 IO
class EventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented('must implement')

    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'Return True if sending is requested'
        return False

    def handle_send(self):
        'Send outgoing data'
        pass

import select

def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()

import socket
import time

class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)

class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)

if __name__ == '__main__':
    handlers = [ UDPTimeServer(('',14000)), UDPEchoServer(('',15000))  ]
    event_loop(handlers)

#test
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'',('localhost',14000))
s.recvfrom(128)
s.sendto(b'Hello',('localhost',15000))
s.recvfrom(128)


class TCPServer(EventHandler):
    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        # Add the client to the event loop's handler list
        self.handler_list.append(self.client_handler(client, self.handler_list))

class TCPClient(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        # Remove myself from the event loop's handler list
        self.handler_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]

class TCPEchoClient(TCPClient):
    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)

if __name__ == '__main__':
    handlers = []
    handlers.append(TCPServer(('',16000), TCPEchoClient, handlers))
    event_loop(handlers)

from concurrent.futures import ThreadPoolExecutor
import os

class ThreadPoolHandler(EventHandler):
    def __init__(self, nworkers):
        if os.name == 'posix':
            self.signal_done_sock, self.done_sock = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self.signal_done_sock = socket.socket(socket.AF_INET,
                                                  socket.SOCK_STREAM)
            self.signal_done_sock.connect(server.getsockname())
            self.done_sock, _ = server.accept()
            server.close()

        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)

    def fileno(self):
        return self.done_sock.fileno()

    # Callback that executes when the thread is done
    def _complete(self, callback, r):

        self.pending.append((callback, r.result()))
        self.signal_done_sock.send(b'x')

    # Run a function in a thread pool
    def run(self, func, args=(), kwargs={},*,callback):
        r = self.pool.submit(func, *args, **kwargs)
        r.add_done_callback(lambda r: self._complete(callback, r))

    def wants_to_receive(self):
        return True

    # Run callback functions of completed work
    def handle_receive(self):
        # Invoke all pending callback functions
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
            self.pending = []

#11  进程间传递 socket 文件描述符  multiprocessing
from multiprocessing.reduction import recv_handle, send_handle
import socket

def worker(in_p, out_p):
    out_p.close()
    while True:
        fd = recv_handle(in_p)
        print('CHILD: GOT FD', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as s:
            while True:
                msg = s.recv(1024)
                if not msg:
                    break
                print('CHILD: RECV {!r}'.format(msg))
                s.send(msg)

def server(address, in_p, out_p, worker_pid):
    in_p.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(address)
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from', addr)
        send_handle(out_p, client.fileno(), worker_pid)
        client.close()

if __name__ == '__main__':
    c1, c2 = multiprocessing.Pipe()
    worker_p = multiprocessing.Process(target=worker, args=(c1, c2))
    worker_p.start()

    server_p = multiprocessing.Process(target=server, args=(('', 20000), c1, c2, worker_p.pid))
    server_p.start()

    c1.close()
    c2.close()


# servermp.py
from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket

def server(work_address, port):
    # Wait for the worker to connect
    work_serv = Listener(work_address, authkey=b'peekaboo')
    worker = work_serv.accept()
    worker_pid = worker.recv()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from', addr)

        send_handle(worker, client.fileno(), worker_pid)
        client.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: server.py server_address port', file=sys.stderr)
        raise SystemExit(1)

    server(sys.argv[1], int(sys.argv[2]))


# workermp.py

from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import os
from socket import socket, AF_INET, SOCK_STREAM

def worker(server_address):
    serv = Client(server_address, authkey=b'peekaboo')
    serv.send(os.getpid())
    while True:
        fd = recv_handle(serv)
        print('WORKER: GOT FD', fd)
        with socket(AF_INET, SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print('WORKER: RECV {!r}'.format(msg))
                client.send(msg)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: worker.py server_address', file=sys.stderr)
        raise SystemExit(1)

    worker(sys.argv[1])


#　 套接字
# server.py
import socket

import struct

def send_fd(sock, fd):
    '''
    Send a single file descriptor.
    '''
    sock.sendmsg([b'x'],
                 [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack('i', fd))])
    ack = sock.recv(2)
    assert ack == b'OK'

def server(work_address, port):
    # Wait for the worker to connect
    work_serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    work_serv.bind(work_address)
    work_serv.listen(1)
    worker, addr = work_serv.accept()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('',port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from', addr)
        send_fd(worker, client.fileno())
        client.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: server.py server_address port', file=sys.stderr)
        raise SystemExit(1)

    server(sys.argv[1], int(sys.argv[2]))

# worker.py
import socket
import struct

def recv_fd(sock):
    '''
    Receive a single file descriptor
    '''
    msg, ancdata, flags, addr = sock.recvmsg(1,
                                             socket.CMSG_LEN(struct.calcsize('i')))

    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS
    sock.sendall(b'OK')

    return struct.unpack('i', cmsg_data)[0]

def worker(server_address):
    serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serv.connect(server_address)
    while True:
        fd = recv_fd(serv)
        print('WORKER: GOT FD', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print('WORKER: RECV {!r}'.format(msg))
                client.send(msg)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: worker.py server_address', file=sys.stderr)
        raise SystemExit(1)

    worker(sys.argv[1])

exit(1)
#10  在网络服务中加入 SSL ssl 模块
KEYFILE = 'privatekey.pem'
CERTFILE = 'cert.pem'
def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'over':
            s.send(b'connection closed')
            break
        s.send(data)
        s.close()
        print('Connection closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)

    while True:
        try:
            c, a = s_ssl.accept()
            print('Got connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))

echo_server(('', 20000))

#test
s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs=CERTFILE)
s_ssl.connect(('localhost', 20000))
s_ssl.send(b'aaaa')
s_ssl.recv()

exit(1)
#9  简单的客户端认证  hmac
import os, hmac
def client_authenticate(connection, secert_key):
    message = connection.recv(32)
    hash = hmac.new(secert_key, message)
    digest = hash.digest()
    connection.send(digest)

def server_authenticate(connection, secert_key):
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secert_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)

#test server
secert_key = b'secertsun'
def echo_handler(client_sock):
    if not server_authenticate(client_sock, secert_key):
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c, a = s.accept()
        echo_handler(c)

echo_server(('', 20000))

#test client
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
client_authenticate(s, secert_key)
s.send(b'hello world')
resp = s.recv(1024)

exit(1)
#8  实现远程方法调用
import pickle
class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass

from multiprocessing.connection import Listener
from threading import Thread
def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

rpc_server(handler, ('localhost', 20000), authkey=b'sun')

#rpc 发送请求的代理类
import pickle
class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())

            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc

from multiprocessing.connection import Client
c = Client(('localhost', 20000), authkey=b'sun')
proxy = RPCProxy(c)
proxy.add(2, 3)
proxy.sub(2, 3)

#7  在不同的 python 解析器之间互动  multiprocessing.connection
from multiprocessing.connection import Listener
import traceback
def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 20000), authkey=b'peekaboo')

exit(1)
# test
from multiprocessing.connection import Client
c = Client(('localhost', 20000), authkey=b'peekaboo')
c.send('hello')
c.recv()

exit(1)
#6  通过 XML-RPC 实现简单的远程调用
from xmlrpc.server import SimpleXMLRPCServer

class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']
    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()

if __name__ == '__main__':
    kvserv = KeyValueServer(('', 20000))
    kvserv.serve_forever()


# test
from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:20000', allow_none=True)
s.set('foo', '123foo')
s.set('bar', [1, 2, 3])
s.keys()
s.get('foo')
s.get('bar')
s.delete('foo')
s.exists('foo')

exit(1)
#5  创建一个简单的 rest 接口
import cgi

def notfound_404(environ, start_response):
    start_response('404 Not found', [('Content-type', 'text/plain')])
    return [b'Not found']

#  调度器
class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(
            environ['wsgi.input'],
            environ=environ
        )
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function

_hello_resp = '''
<html>
   <head>
       <title>Hello {name}</title>
   </head>
   <body>
     <h1>Hello {name}!</h1>
   </body>
</html>
'''

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')

_localtime_resp = '''\
 <?xml version="1.0"?>
 <time>
   <year>{t.tm_year}</year>
   <month>{t.tm_mon}</month>
   <day>{t.tm_mday}</day>
   <hour>{t.tm_hour}</hour>
   <minute>{t.tm_min}</minute>
   <second>{t.tm_sec}</second>
 </time>
'''
def localtime(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/xml') ])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_world)
    dispatcher.register('GET', '/localtime', localtime)

    httpd = make_server('', 5000, dispatcher)
    print('Serving on port 5000...')
    httpd.serve_forever()

exit(1)
#4  通过 CIDR 地址生成对应的 IP 地址集  ipaddress 模块
import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
print(net) # IPv4Network('123.45.67.64/27')
for n in net:
    pass
#print(n)

print(net.num_addresses)        #32
print(net[0])                   #123.45.67.64
print(net[net.num_addresses-1]) #123.45.67.95

a = ipaddress.ip_address('123.45.67.65')
print(a in net) # True
b = ipaddress.ip_address('123.45.67.96')
print(b in net) # False

inet = ipaddress.ip_interface('123.45.67.64/27')
print(type(inet)) #<class 'ipaddress.IPv4Interface'>
print(inet.network) #123.45.67.64/27 str()
print(inet.ip) #123.45.67.64

exit(1)
#3  创建 UDP 服务器
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()

exit(1)

#2  创建 tcp 服务器  socketserver
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

class StreamHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler) # 单用户
    #serv = ThreadingTCPServer(('', 20000), EchoHandler) 多用户
    serv.serve_forever()

# security action
if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serve_forever)
        t.daemon = True
        t.start()
        serv.serve_forever

#  服务器实现
from socket import socket, AF_INET, SOCK_STREAM
def echo_handler(address, client_sock):
    print('Got connetction from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
        client_sock.close()

def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)

if __name__ == '__main__':
    echo_server(('', 20000))

exit(1)
#1  作为客户端与 ｈｔｔｐ 服务交互 　 测试站点  http://httpbin.org
url = 'http://127.0.0.1:5000/'

params = {
    'name1': 'name1value',
    'name2': 'name2value'
}

querystring = parse.urlencode(params)

# GET
u = request.urlopen(url + '?' + querystring)
resp = u.read()
print(resp)

# POST
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()
print(resp)

# header
headers = {
     'User-agent': 'none/ofyourbusiness',
     'Spam': 'Eggs',
     'Token': 'aaaaaaaa'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp = u.read()
print(resp)

# requests  库
resp = requests.post(url, data=params, headers=headers)
text = resp.text
print(text)

# headers
resp = requests.head('https://www.python.org/')
print(resp.status_code)
#print(resp.headers['last-modified'])
print(resp.headers['content-type'])
print(resp.headers['content-length'])

# login auth
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user','password'))
print(resp)

# cookies
resp1 = requests.get('https://www.python.org/')
resp2 = requests.get('https://www.python.org', cookies=resp1.cookies)

# files
files = {'file': ('data.csv', open('tmp/data.d', 'rb'))}
resp = requests.post(url, files=files)
print(resp)

#　 底层库  http.client
from http.client import HTTPConnection

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/')
resp = c.getresponse()
print('status:', resp.status)
for name, value in resp.getheaders():
    print(name, ':', value)

#　 实现 auth
auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = urllib.request.build_opener(auth)

r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()
