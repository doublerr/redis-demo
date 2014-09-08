import datetime
import redis
import tornado.ioloop
import tornado.web
import os


class MessageHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.redis = redis.StrictRedis(
            host=os.environ['REDIS_PORT_6379_TCP_ADDR'],
            port=os.environ['REDIS_PORT_6379_TCP_PORT'],
        )

    def get(self):
        messages = sorted([(_, self.redis.get(_)) for _ in self.redis.keys()], key = lambda _: _[0], reverse = True)

        loader = tornado.template.Loader(os.path.dirname(__file__))
        self.write(loader.load('input-form.html.jinja').generate(m=messages))

    def post(self):
        self.redis.set(
            datetime.datetime.now(),
            self.get_argument('message')
        )

        self.redirect('/')

application = tornado.web.Application([
    (r"/", MessageHandler),  # POST / - new message; GET / - list messages
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
