#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 10:03:44 2025

@author: haojiacheng
"""

# arr = [[0]*10]*10
# for  x in range(1 , 11):
#     for i in range(1 , x):
#         arr[x][i] = [x][i]

# dic = {"abc" : 123 , "xyz" :234}
# def a(dic):
#     x = ""
#     for i  in dic:
#         x +=str(dic[i]) 
        
#     return x.strip()


# y = a(dic)
# print(type(y))

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 88, 92]
}
df = pd.DataFrame (data)
print(df)

print(df["Name"])
print(df.iloc[0])
