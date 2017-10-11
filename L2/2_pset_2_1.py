# -*- coding: utf-8 -*-
'''
created on Oct 11 16:09 2017
@author:wille woud
'''

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
	print(month_Pay-10)
