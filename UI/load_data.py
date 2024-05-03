# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:50:41 2024

@author: dayas
"""
import json

def load_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data