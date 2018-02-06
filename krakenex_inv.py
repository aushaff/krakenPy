# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:03:45 2017

@author: austin
"""

import krakenex
from pykrakenapi import KrakenAPI
#import os

api = krakenex.API()
key ="ignored/new_key.key"
api.load_key(key)

api.query_private(method = "Balance")

k = KrakenAPI(api)

k.get_account_balance()
k.get_trades_history()


ohlc, last = k.get_ohlc_data("BCHUSD")
print(ohlc)
print(last)

# open trade
descr = k.add_standard_order(pair = "XBTEUR", type = "buy", ordertype = "market", volume = 0.002)
descr
k.get_open_orders(trades = True)
k.get_tradable_asset_pairs()


help(KrakenAPI)



ret = k.query_private("Balance")

k.secret
