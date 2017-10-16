# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:25:37 2017

@author:  willie_woud
#@email:   tywzzw@163.com
@website: https://github.com/williewould
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    new_aTup=()
    for i in range(len(aTup)):
        if i%2==0:
            new_aTup+=(aTup[i],)
    #print(new_aTup)
    return new_aTup
aTup=('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))