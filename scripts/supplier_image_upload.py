#!/usr/bin/env python3

import requests
import os

url = "http://35.192.136.11/upload/"
path = os.path.expanduser('~') + '/supplier-data/JPEG_images/'

for file in os.listdir(path):
    with open(path+file,'rb') as upload_im:
        r = requests.post(url, files = {'file':upload_im})


