# -*- coding: utf-8 -*-
'''
created on Oct 11 16:09 2017
@author:wille woud
'''
def reamain_Balance(balance,annualInterestRate,monthlyPaymentRate):
'''
input: balance,annualInterestRate,monthlyPaymentRate
output: remaining balance  计算本月剩余的本金【即上个月的剩余本金+上个月剩余本金*利息】
'''
    monthlyInterestRate=annualInterestRate/12
    month=12
    def un_Balance_cal(month):
        if month==0:
            un_Balance=balance-balance*monthlyPaymentRate
            return un_Balance
        else:
			# The remain balance this moth include balance and interestes
            remain_Balance=un_Balance_cal(month-1)+monthlyInterestRate*un_Balance_cal(month-1)
			# un_Balance is money  you don't pay next moth
            un_Balance=remain_Balance-remain_Balance*monthlyPaymentRate
        return un_Balance
    
    #return round(un_Balance_cal(month)/(1-monthlyPaymentRate),2)
    print('Remaining balance: '+str(round(un_Balance_cal(month)/(1-monthlyPaymentRate),2)))
