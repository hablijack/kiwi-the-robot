#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler


class Independant(RequestHandler):

    def initialize(self, kiwi):
        self.kiwi = kiwi

    def post(self):
        state = self.get_argument('independant')
        if state == "true":
            self.kiwi.set_operation_mode('independant')
        else:
            self.kiwi.set_operation_mode('waiting_for_command')
