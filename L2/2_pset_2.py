# -*- coding: utf-8 -*-
'''
created on Oct 11 16:09 2017
@author:wille woud
'''
def fixed_b(balance,annualInterestRate):
    """
    input:balance,annualInterestRate
    output: Lowest Payment erery month
    每个月还固定本金，生成下月未还本金*（1+月利息）=下月应还本金
    当下月应还本金 up <0 时循环终止，
    """
    month_Pay = 10
    an_Rate=annualInterestRate
    up=balance
    while up >= 0:
        up=balance
    for i in range(12):
        up=(up-month_Pay)*(1+an_Rate/12)
        month_Pay+=10
        print(up)
	#at last month_Pay add more one times so we substrate 10 here
    print(month_Pay)
