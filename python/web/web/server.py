from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8888, application)
print('Server is starting...')
httpd.serve_forever()
