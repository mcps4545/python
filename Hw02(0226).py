# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:13:59 2021

@author: admin
"""
'''
用FOR迴圈印出以下:
    123456789
    12345678
    1234567
    123456
    12345
    1234
    123
    12
    1
'''
for a in range(9,0,-1):    
    for b in range(1,a+1):
        print(b,end="")
    print()
    
