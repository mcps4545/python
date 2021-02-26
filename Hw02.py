# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:57:43 2021

@author: USER
"""
'''
1100224HW02:
    輸入迴圈次數，計算數值中為偶數的總和
    ，最後印出加總的值。
'''
total=0
number =int(input("請輸入數字:"))
for a in range(1,number+1):
    if a%2 == 0:
        total += a
print("加總值:",total)
print("程式執行完畢"
