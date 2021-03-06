#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tornado
from kiwi import Kiwi
from server.webserver import WebServer


if __name__ in '__main__':
    kiwi = Kiwi('command')
    kiwi.start_to_exist()
    WebServer(kiwi).serve()
    tornado.ioloop.IOLoop.current().start()


    #xServo = Servo(0, 'xServo', _zero=101)
    #yServo = Servo(1, 'yServo', _zero=101)
    #zServo = Servo(2, 'zServo', _zero=90)

    # xServo.reset()
    # yServo.reset()
    #xServo.setPauseWhenDone(2)
    #xServo.setSpeedStep(1)
    #xServo.setSleepDelay(0.01)
    #xServo.reset()

    #yServo.setPauseWhenDone(2)
    #yServo.setSpeedStep(1)
    #yServo.setSleepDelay(0.01)
    #yServo.reset()

    #zServo.setPauseWhenDone(2)
    #zServo.setSpeedStep(1)
    #zServo.setSleepDelay(0.01)
    #zServo.reset()

    #print('Moving Servos around ...')
    #while True:
    #    xServo.setDegrees('+10')
    #    xServo.go()#

        #yServo.setDegrees('+20')
        #yServo.go()

        #xServo.setDegrees('-10')
        #xServo.go()

        #zServo.setDegrees('+15')
        #zServo.go()

        #yServo.setDegrees('-20')
        #yServo.go()

        #zServo.setDegrees('+30')
        #zServo.go()

        #zServo.setDegrees('-90')
        #zServo.go()

        #zServo.setDegrees('+45')
        #zServo.go()
