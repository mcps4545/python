# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:14:51 2021

@author: admin
"""
'''
由使用者輸入數值，請透過FOR將1~數值作加總，最後印出總和。
'''
a=int(input("請輸入數值:"))
total=0
for b in range(1,a+1):
    total += b
print(total)
print("程式執行完畢")
    