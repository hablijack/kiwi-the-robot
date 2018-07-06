#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler


class HomepageHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render('index.html')
