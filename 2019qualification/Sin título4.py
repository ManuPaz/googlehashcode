#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:27:22 2022

@author: manuel
"""

tam=1000000
a=range(tam)
import time
tiempo1=time.time()
l=0
for u in a:
    l+=u
        
        
tiempo2=time.time()
print("Tiempo %s, %s"%(tiempo2-tiempo1,l))