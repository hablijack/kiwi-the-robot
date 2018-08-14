#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lib.logger import Logger
from tornado.ioloop import IOLoop
from lib.sound_effect import SoundEffect
from tornado import gen
import datetime
import lib.config as config


class Kiwi():

    operation_mode = ''
    command_to_execute = ''

    def __init__(self, start_mode):
        Logger.log('Initializing the kiwi system, press Ctrl-C to quit...')
        SoundEffect.play('hello')
        self.operation_mode = config.get('kiwi', 'start_mode')

    def set_operation_mode(self, mode, command=None):
        Logger.log('Received order for operation-mode change. Going to: ' + mode + ' mode...')
        self.operation_mode = mode
        self.command_to_execute = command

    @gen.coroutine
    def start_to_exist(self):
        while True:
            if self.operation_mode == "independant":
                timeout = self.operate_independant()
            elif self.operation_mode == 'command':
                timeout = self.operate_on_command()
            elif self.operation_mode == 'sleep':
                timeout = self.go_to_sleep()
            elif self.operation_mode == 'waiting_for_command':
                timeout = 500
            yield gen.Task(
                IOLoop.current().add_timeout, datetime.timedelta(milliseconds=timeout)
            )

    def operate_independant(self):
        Logger.log("Alright, then i'll do what i want :-P")
        return 500

    def operate_on_command(self):
        Logger.log("Yes, master. I'm executing your order: " + self.command_to_execute)
        self.operation_mode = 'waiting_for_command'
        return 500
