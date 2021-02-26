# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:55:19 2021

@author: USER
"""
'''
110024HW01:
    輸入迴圈次數，判斷哪些數值是奇數，那些是偶數。
'''
number =int(input("請輸入數字:"))
for a in range(1,number+1):
    if a%2 != 0:
        print(a,end=(","))
print("以上數字為奇數")
for a in range(1,number+1):
    if a%2 == 0:
        print(a,end=(","))
print("以上數字為偶數")
print("程式執行完畢")
