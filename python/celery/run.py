import tornado.ioloop
import tornado.web
from scheduler import get


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html = '''<form action="/" method="post">
              <p><input name="url"></p>
              <p><button type="submit">Start</button></p>
              </form>'''
        self.write(html)

    def post(self):
        url = self.get_argument("url")
        title = get(url)
        return self.write(title)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
