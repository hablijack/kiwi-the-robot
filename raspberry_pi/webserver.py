#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tornado
from lib.logger import Logger
from homepage_handler import HomepageHandler
from tornado.web import Application
import lib.config as config
import os

rel = lambda *x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))


class WebServer():

    def __init__(self):
        pass

    def serve(self):
        settings = dict(
            template_path=rel('./web/templates'),
            static_path=rel('./web'),
            debug=True
        )
        app = Application([
            (r"/", HomepageHandler),
        ], **settings)

        http_server = tornado.httpserver.HTTPServer(app)
        port = config.get('server', 'port')
        http_server.listen(port=port)
        Logger.log("... Webserver ist erreichbar unter 127.0.0.1:{}.".format(port))
