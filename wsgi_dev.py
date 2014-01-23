# !usr/bin/python
"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys

# Activate your virtual env
activate_env = os.path.expanduser(
    "/home/intip/.virtualenvs/dark/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/intip/ET/dark-ride/project/')

from project.wsgi import *

