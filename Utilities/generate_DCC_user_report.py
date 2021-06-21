#!/usr/bin/env python3

import DCC
import Config as CF

# This script searches for users in DCC and outputs the results to a tab-delimited text file

#requires edits to DCC.py to include the isActive property in search results, and return it in the list:
# change ln 947           '''<username/><first_name/><last_name/><email/><mailstop/><phone/><isActive/>''' \
# add ln 991       ud['isactive'] = res.isactive.text




# Login to DCC
s = DCC.login(Site = 'Production') 
r = DCC.user_search(s, username = '*')

filename = CF.reportfilepath + 'userlist_tab_delimited.csv'

f = open(filename, 'w')
f.write('handle \t username \t first_name \t last_name \t email \t phone \t isactive\n')

for i in r:
    f.write(i['handle'] + "\t" + i['username'] + "\t" + i['first_name'] + "\t" + i['last_name'] + "\t" + i['email'] + "\t" + i['phone'] + "\t" + i['isactive'] + "\n")
    
f.close()

