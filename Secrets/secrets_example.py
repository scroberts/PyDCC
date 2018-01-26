#!/usr/bin/env python3

# COPY THIS FILE TO secrets.py IN THIS FOLDER AND EDIT TO ADD YOUR LOGIN CREDENTIALS
# This file stores passwords etc.  
# !!!Do not sync your secrets.py file to at GitHub repository!!!
# !!!Do not share your secrets.py file with anyone


# DCC Production Passwords
## Enter any number of username & password pairs here with different names as below
DCC_reg = {'login':'USERNAME', 'password':'PASSWORD'}
DCC_adm = {'login':'USERNAME', 'password':'PASSWORD'}
## DCC Test site Passwords
# This is the general password used for DCC Test
DCC_test = {'login':'USERNAME', 'password':'PASSWORD'}

# TraceTree Passwords
## Enter your TraceTree login credentials here
TT = {'login':'USERNAME', 'password':'PASSWORD'}

# Define password structure
## Enter the password set names from above that you want to use to login here for DCC, 
## TT (TraceTree), and the DCC test site. For example:

pw = {'DCC':DCC_reg, 'TT':TT, 'DCCTest':DCC_test}