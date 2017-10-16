# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:05:31 2017

@author:  willie_woud
@email:   tywzzw@163.com
@website: https://github.com/williewould
"""
def applyEachTo(L, x):
    """
    把函数放入list 分别对x运算
    the function can be the element of the list. You can apply them by for loop
    and () to caculate the value.
    """
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))