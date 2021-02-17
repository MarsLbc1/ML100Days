# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 00:49:50 2021

@author: user
"""

import numpy as np

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a=np.arange(1,21,1)
print(a)

#2.呈上題，將以上數列取出偶數。
b=np.arange(1,21,1)
print(b)
i=0
while i <= 9:
    print(b[2*i+1])
    i=i+1
    
#3.呈1題，將數列取出3的倍數。
c=np.arange(1,21,1)
print(c)
i=0
while i <= 18:
    i += 1
    if b[i] % 3 != 0:
        continue    
    print(i+1)        