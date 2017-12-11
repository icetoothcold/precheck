# -*- coding: utf-8 -*-
__author__ = 'Lyan'


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ASYNCMODE= None
    BASEHOST = "10.221.155.200"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

