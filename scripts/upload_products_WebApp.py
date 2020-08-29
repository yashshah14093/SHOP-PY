#!/usr/bin/env python3

from upload_objects import upload_object
import os

def upload_products(dict_names):

    path = "/mnt/c/Users/91894/Desktop/SHOP-PY/supplier-data/descriptions/"

    for file in os.listdir(path):
    
        file_name,extension = file.split(".")
    
        if(file_name in dict_names):
    
            with open(path+file) as file_to_read:
                input = file_to_read.readline
                name = input()

                weight_string = input()
                weight_list = weight_string.split(" ")
                quantity = int(weight_list[0])
                
                image = "img/"+file_name+".jpeg"

                description = input()
                
                upload_object(name,quantity,image,description)

