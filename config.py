# -*- coding: utf-8 -*-

import os
from datetime import timedelta

__basedir__ = os.path.abspath(os.path.dirname(__file__))

PROJECT_NAME = 'empty_flask_app'

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///../' + PROJECT_NAME+'.db'
SQLALCHEMY_ECHO = True

# security
CSRF_ENABLED = True
SECRET_KEY = "secret_key"  # import os; os.urandom(24)
LOGGER_NAME = "%s_log" % PROJECT_NAME
PERMANENT_SESSION_LIFETIME = timedelta(days=1)
