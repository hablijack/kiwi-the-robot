#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

def get(section, name):
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read('./settings.ini')
    return settings.get(section, name)

def verbose():
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read('./settings.ini')
    return settings.get('logging', 'verbose').lower() in ("yes", "true", "t", "1")
