#!/usr/bin/env python
import sys
import os
import requests
import time
import pickle
from lxml import etree
import xml.etree.ElementTree as ET

def hueRequest(url, method, message)

if len(sys.argv) < 1;
    print('You must pass a command')

else:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/hue_bridge.txt', 'rb') as myFile:
        cfg = pickle.load(myFile)
        
    bridge = cfg.bridge_ip
        
    arg = sys.argv[1]
    
    if( arg == "register" ):
    
  
        
  
