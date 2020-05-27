#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import handlers.websocket
from jinja2 import Template
from tornado.options import define, options

from caverimx.helpers import TemplateLoader

define("port", default=4311, help="run on the given port", type=int)

settings={
    'static_path':'/recursos/public',
}

template_loader = TemplateLoader('/recursos/vistas')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        template = template_loader.get('landing/index.pyml')
        self.write(template.render(env=os.environ))
 
def main():
    tornado.options.parse_command_line()
    
    application = tornado.web.Application([
        
        (r"/websocket",handlers.websocket.WebSocket),
        (r"/index.py", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path']) ),
        ], **settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()