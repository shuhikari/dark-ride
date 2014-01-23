# !usr/bin/python
"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

# Add the site-packages of the chosen virtualenv to work with
# asite.addsitedir('/home/intip/.virtualenvs/dark/lib/python2.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/intip/ET/dark-ride/project/')

# Activate your virtual env
activate_env = os.path.expanduser(
    "/home/intip/.virtualenvs/dark/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
