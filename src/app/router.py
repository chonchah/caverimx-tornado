import handlers.websocket
import tornado.web
import handlers.websocket, handlers.home
settings={
    'static_path':'/recursos/public',
}

routes=[
    (r"/websocket",handlers.websocket.WebSocket),
    (r"/",handlers.home.MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path']) ),
]