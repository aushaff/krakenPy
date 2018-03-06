#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:20:58 2018
Script to create various stop losses for krakenexchange
a) stop to sell all at certain cash level
b) stop to sell each asset at a certain cash level
c) trailing stop for the account (sell all at certain % drop)
d) trailing stop for each asset (sell asset at certain % drop)

@author: deckard
"""

import krakenex
import os
import time

# =============================================================================
# Script working
# (a) Hard stop to prevent loss of capital
# Initially one that takes account balance and cashes everything 
# out when less than a certain value.
# TODO:
# 1) What errors need to be caught

# set mininum account balance
min_bal = 100000
invested = True
pause_period = 60 # seconds

# location of the api keys
api_dir ="/home/austin/Dropbox/kraken_data/api"
k = krakenex.API() # start api instance and load keys
k.load_key(os.path.join(api_dir, 'kraken.key'))

while(invested):

    # get the current balance
    curr_bal = k.query_private('Balance')

    # if the current balance is below our minimum
    if (curr_bal < min_bal): 
 
        # get open positions
        # START: this code is copied verbatim from 
        # https://github.com/veox/python3-krakenex/blob/master/examples/print-open-positions.py
        
        # prepare request
        req_data = {'docalcs': 'true'}

        # querry servers
        start = k.query_public('Time')
        open_positions = k.query_private('OpenPositions', req_data)
        end = k.query_public('Time')
        latency = end['result']['unixtime']-start['result']['unixtime']
        
        # parse result
        dict(open_positions)
        
        b = 0
        c = 0
        for i in open_positions['result']:
            order = open_positions['result'][i]
            if(order['pair']=='XETHZUSD'):
                b += (float(order['vol']))
            if (order['pair'] == 'XXBTZUSD'):
                c += (float(order['vol']))
        
        print('error count: ' + str(len(open_positions['error'])))
        print('latency: ' + str(latency))
        print('total open eth: ' + str(b))
        print('total open btc: ' + str(c))
        print('total open positions: ' + str(len(open_positions['result'])))
        # STOP COPY        
        
        # asset_list = sort_asset_list(largest_first)
        # exch_all_assets_for_euro(asset_list)}
        # for each asset:
        # if(paired_with_euro)
        # exch_for_euro(curr) & invested(false)
        
        # else {
        # exch_for_xbt(curr)
        # exch_for_eur(xbt) & invested(false)
        
    elif (curr_bal > min_bal):
        
        # pause for pause_period
        time.sleep(pause_period)
        
    else:
        
        # provide an error that system is not functiong!
    
        
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# (b) then one that takes euro value of each asset and cashes out at certain value
# 
# while(have_invs):
# 
# # get(min_asset_val) # list
# # get_asset_list
# # if L(asset_list) <L(min_asset_val)
# # find(missing_asset_name)
# # alert missing_asset_name)
# # for each asset:
# # if(curr_ass_val < ass_min_val)
# #... As before cash out
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ‌(c) then trailing stop for the account
# perc_trail = ...
# Replace if(curr_bal<min_bal)
# get_balance_max(time_period)
# diff = (max_balance/100)*perc_trail
# If(curr_bal<(max_ba-diff)
# # as before sell
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# (d) ‌then trailing stop for each asset
# 
# Same as (b) except sub (c)
# 
# =============================================================================
