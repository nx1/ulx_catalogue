#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:39:19 2019

@author: nk7g14
"""
from astroquery.heasarc import Heasarc
from astroquery.vizier import Vizier
import pandas as pd
import time

class ULX():
    '''This class is used to for the creation of ULX objects 
    '''
    def __init__(self, name, ra, dec, host, ulx_num, candidate):
        self.name = name
        self.ra = ra
        self.dec = dec
        self.host = host
        self.ulx_num = ulx_num
        self.candidate = candidate

h = Heasarc()
v = Vizier()
v.ROW_LIMIT = -1




# =============================================================================
# Useful Commands
'''
table.show_in_browser(jsviewer=True)
h_mission_list = h.query_mission_list()
'''
# =============================================================================
  cxogsgsrc
#'cxogsrc','xmmmaster',
#Heasarc ULX tables:
ht = ['ulxngcat',  'm51cxo', 'ngc1332cxo', 'ngc1600cxo', 'numaster',
      'fornaxacxo', 'm31cfcxo', 'm51cxo2', 'm83xmm', 'maxigschgl', 'rass2foid',
       'xmmssclwbs', 'vlulxcat', 'ulxrbcat', 'xray',  'chanulxcat',
      'chngpscliu', 'cxogsgsrc']

#Vizier ULX tables:
vt = ['J/A+A/429/1125',
 'J/A+A/452/739',
 'J/A+A/493/339',
 'J/A+A/555/A65',
 'J/A+A/575/A42',
 'J/AJ/143/144',
 'J/AJ/150/94',
 'J/ApJ/586/826',
 'J/ApJ/601/735',
 'J/ApJ/617/262',
 'J/ApJ/649/730',
 'J/ApJ/664/458',
 'J/ApJ/687/471',
 'J/ApJ/699/453',
 'J/ApJ/719/L79',
 'J/ApJ/725/842',
 'J/ApJ/741/49',
 'J/ApJ/741/86',
 'J/ApJ/749/130',
 'J/ApJ/756/27',
 'J/ApJ/758/105',
 'J/ApJ/777/7',
 'J/ApJ/786/20',
 'J/ApJ/797/91',
 'J/ApJ/813/28',
 'J/ApJ/825/7',
 'J/ApJ/827/46',
 'J/ApJ/829/20',
 'J/ApJS/143/25',
 'J/ApJS/154/519',
 'J/ApJS/157/59',
 'J/ApJS/166/211',
 'J/ApJS/177/465',
 'J/ApJS/179/142',
 'J/ApJS/192/10',
 'J/ApJS/212/9',
 'J/ApJS/218/9',
 'J/ApJS/222/12',
 'J/MNRAS/344/134',
 'J/MNRAS/388/849',
 'J/MNRAS/416/1844',
 'J/MNRAS/446/470',
 'J/PASJ/63/S677']
# 'J/ApJS/224/40', MASSIVE TABLE


'''
tab_dict = {}
for t in vt:
    print(t)
    tab_dict[t] = v.get_catalogs(t)
    time.sleep(0.2)

for i in ht:
    print(i)
    tab_dict[i] = h.query_object('', mission=i, fields='All')
'''   

print('{} {}'.format('mission', 'len'))
for i in tab_dict:
    length = str(len(tab_dict[i]))
    print('{} {}'.format(i, length))
    #print(tab_dict[i])
    
    
    
'''
for t in vt2:
    print(t)
    t.show_in_browser(jsviewer=True)
'''