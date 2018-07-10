#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler


class Homepage(RequestHandler):

    def initialize(self, kiwi):
        self.kiwi = kiwi

    def get(self):
        self.render('index.html', operation_mode=self.kiwi.operation_mode)
