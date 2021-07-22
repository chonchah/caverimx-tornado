import handlers.websocket
import tornado.web
import handlers.websocket
import handlers.home
settings = {
    'static_path': '/recursos/public',
}

routes = [
    (r"/websocket", handlers.websocket.WebSocket),
    (r"/api", handlers.home.MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
]
