# -*- coding: utf-8 -*-
# 引用a b ， a b 均是函数名称 
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
