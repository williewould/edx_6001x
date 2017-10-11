# -*- coding: utf-8 -*-
'''
created on Oct 11 16:09 2017
@author:wille woud
'''


def fixed_b(balance, annualInterestRate):
    '''
    input:balance,annualInterestRate
    output: Lowest Payment erery month
    每个月还固定本金，生成下月未还本金*（1+月利息）=下月应还本金
    当下月应还本金 up <0 时循环终止，
    '''

    an_Rate = annualInterestRate
    up = balance
    l_month_Pay = balance/12
    h_month_Pay = (balance*(1+an_Rate)**12)/12
    month_Pay = (l_month_Pay+h_month_Pay)/2
    while up >= 0.01 or up <= -0.01:
        up = balance
        month_Pay = (l_month_Pay+h_month_Pay)/2
        # month_Pay=round(month_Pay,2)
        for i in range(12):
            up = (up-month_Pay)*(1+an_Rate/12)
        if up >= 0.01:
            l_month_Pay = month_Pay
        if up < 0.01:
            h_month_Pay = month_Pay
        print(up)
        # last month_Pay add more one times so we substrate 10 here
    print('Lowest Payment: '+str(round(month_Pay, 2)))
fixed_b(3000, 0.2)
