import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\n Host: www.sina.com.cn\r\n Connection: close\r\n\r\n')

buffers = []
while True:
    d = s.recv(1024)
    if d:
        buffers.append(d)
    else:
        break

data = b''.join(buffers)
s.close

header, html = data.split(b'\r\n\r\n', 1)
print(header)

with open('sina.html', 'wb') as f:
    f.write(html)
