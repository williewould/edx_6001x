# -*- coding: utf-8 -*-
# 字符串切片问题
'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
s = 'azcbobobegghakl'
n_bob=0
for i in range(len(s)):
    if s[i:i+3]=='bob':
        n_bob+=1
print('Number of times bob occurs is: '+str(n_bob))
    
