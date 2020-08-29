
import django
import sys
import subprocess
import os

def SystemSetup():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    sys.path.append("/mnt/c/Users/91894/Desktop/SHOP-PY/Shop-py/WebApp")
    sys.path.append("/mnt/c/Users/91894/Desktop/SHOP-PY/Shop-py/WebApp/WebApp")
    django.setup()


