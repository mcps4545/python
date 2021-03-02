# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:06:55 2021

@author: admin
"""
'''
印出以下:
1
12
123
1234
'''
for a in range(1,5):
    for b in range(1,a+1):
        print(b,end="")
    print()
