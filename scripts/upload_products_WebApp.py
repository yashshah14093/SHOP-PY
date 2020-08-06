#!/usr/bin/env python3

import os
import requests

path = os.path.expanduser('~') + "/supplier-data/descriptions/"
url = "http://35.192.136.11/fruits/"


for file in os.listdir(path):
    
    f,e = file.split(".")
    obj = {"image_name":f+".jpeg"}
    
    with open(path+file) as file_to_read:
        input = file_to_read.readline
        name = input()

        weight_string = input()
        weight_list = weight_string.split(" ")
        # print(weight_list)
        weight = int(weight_list[0])

        description = input()

        obj["name"] = name
        obj["weight"] = weight
        obj["description"] = description

        response = requests.post(url,json=obj)
        # print(response.status_code,response.ok)
