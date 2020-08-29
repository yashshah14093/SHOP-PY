#!/usr/bin/env python3
import os
import re
import PIL.Image

def uploadImages():

    old_path = '/mnt/c/Users/91894/Desktop/SHOP-PY/supplier-data/images/'
    new_path = '/mnt/c/Users/91894/Desktop/SHOP-PY/Shop-py/WebApp/media/img/'
    
    dict_names = {}
    
    for file in os.listdir(old_path):
    
        format = ".tiff$"
        image_tiff = re.search(format,file)
    
        if image_tiff : 
            image_name,extension = file.split(".")
            dict_names[image_name] = 1
            image_name = image_name + ".jpeg"
            Image_old = PIL.Image.open(old_path+file)
            Image_new = Image_old.resize((400,400)).convert("RGB")
            Image_new.save(new_path+image_name,'jpeg')

    return dict_names
