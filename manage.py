# -*- coding: utf-8 -*-
__author__ = 'Lyan'

import os
from app import create_app
from flask_script import Manager
from flask_socketio import SocketIO

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()