'''
ssume s is a string of lower case iacters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
逐个比 相邻是元素大小， 如果是一直大 就增
否则 归0 重新计数
直到最后一个元素
'''
# -*- coding: utf-8 -*-
s='abdoefghijkl'
count = 0
maxcount = 0
result = 0

for i in range(len(s) - 1):
    if (s[i] <= s[i + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            result = i + 1 #计算终点 和距离
    else:
        count = 0
startposition = result - maxcount # 利用终点 和距离计算起点
print('Longest substring in alphabetical order is:', s[startposition:result + 1])
