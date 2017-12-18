# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:03:45 2017

@author: austin
"""

import krakenex
import os

api_dir ="/home/austin/Dropbox/kraken_data/api"

k = krakenex.API()
k.load_key(os.path.join(api_dir, 'kraken.key'))

ret = k.query_private("Balance")

k.secret
