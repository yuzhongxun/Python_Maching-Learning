# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:58:29 2018

@author: Zhong-Xun Yu
"""

import pandas as pd

groups = ["Working", "Dancing", "cooking",
        "Movies", "Sports", "Finishing"]
num = [12, 15, 3, 8, 29, 38]

dict = {"groups" : groups,
        "num" : num
        }

mydf = pd.DataFrame(dict)
print(mydf.iloc[:,:])    # iloc 來選取所有列和欄
print("------")
print(mydf.iloc[0, 1])   # 第一列第二欄 : 組的人數
print("------")
print(mydf.iloc[0:2, :])   # 第一列和第二列 : 組的組名與人數
print("------")
print(mydf.iloc[:,0])   # 第一欄 : 各組的人數
print("------")
print(mydf["num"])    # 各組的人數
print("------")
print(mydf.num)       # 各組的人數