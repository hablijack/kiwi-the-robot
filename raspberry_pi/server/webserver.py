#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tornado
from lib.logger import Logger
from server.handler.homepage import Homepage
from server.handler.emotions import Emotions
from server.handler.freehand import Freehand
from server.handler.independant import Independant
from server.handler.settings import Settings
from tornado.web import Application
import lib.config as config
import os

rel = lambda *x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))


class WebServer():

    def __init__(self, kiwi):
        self.kiwi = kiwi

    def serve(self):
        settings = dict(
            template_path=rel('./web/templates'),
            static_path=rel('./web'),
            debug=True
        )
        app = Application([
            (r"/", Homepage, dict(kiwi=self.kiwi)),
            (r"/emotion", Emotions, dict(kiwi=self.kiwi)),
            (r"/freehand", Freehand, dict(kiwi=self.kiwi)),
            (r"/independant", Independant, dict(kiwi=self.kiwi)),
            (r"/settings", Settings, dict(kiwi=self.kiwi)),
        ], **settings)

        http_server = tornado.httpserver.HTTPServer(app)
        port = config.get('server', 'port')
        http_server.listen(port=port)
        Logger.log("... kiwi GUI is serving under 127.0.0.1:{}.".format(port))
