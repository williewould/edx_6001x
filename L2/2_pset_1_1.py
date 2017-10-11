# -*- coding: utf-8 -*-
'''
created on Oct 11  2017
@author:wille woud
'''
monthlyInterestRate=annualInterestRate/12
month=12
def ub_cal(month):
	if month==0:
		ub=balance-balance*monthlyPaymentRate
		#print(ub)
		return ub
	else:
		b=ub_cal(month-1)+monthlyInterestRate*ub_cal(month-1)
		#print(b)
		ub=b-b*monthlyPaymentRate
		#print(str(month)+':'+str(ub))
	return ub

#return round(ub_cal(month)/(1-monthlyPaymentRate),2)
print('Remaining balance: '+str(round(ub_cal(month)/(1-monthlyPaymentRate),2)))
