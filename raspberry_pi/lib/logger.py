#!/usr/bin/python
# -*- coding: utf-8 -*-

import lib.config as config

class Logger():

    @staticmethod
    def log(message):
        if config.verbose():
            print(message)
