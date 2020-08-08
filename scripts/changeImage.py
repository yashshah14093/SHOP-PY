#!/usr/bin/env python3

import os
import re
from PIL import Image

old_path = os.path.expanduser('~') + '/supplier-data/images/'
new_path = os.path.expanduser('~') + '/supplier-data/'

for file in os.listdir(old_path):
    
    s = ".tiff$"
    x = re.search(s,file)
    
    if x : 
        f,e = file.split(".")
        f = f + ".jpeg"
        im = Image.open(old_path+file)
        new_im = im.resize((600,400)).convert("RGB")
        new_im.save(new_path+"images/"+f,'jpeg')
