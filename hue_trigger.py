#!/usr/bin/env python
import sys
import os
import requests
import time
import json

import hue_config.py as cfg

def hueRequest(url, method, message):
    

if len(sys.argv) < 2;
    print('You must pass a command')

else:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    bridge_ip = cfg.bridge_ip
    username = cfg.username
    baseurl = 'http://' + bridge_ip + '/api/' + username + '/lights'
        
    arg = sys.argv[1].lower()
    arg = arg.lstrip()
    
    if( arg == "state" ):
        try:
            response = requests.get(baseurl, timeout=2)
            content = response.read()
            data = json.loads(content)
            print data
        except requests.RequestException, e:
            print e
        

  
        
  
