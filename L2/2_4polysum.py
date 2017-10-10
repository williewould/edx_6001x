# -*- coding: utf-8 -*-
'''
created on Oct 10 20:50:50 2017
@author:wille woud
'''
def polysum(n,s):
'''
input:
Enter 'n' that is number of sides of regular polygon. 
Enter 's' that is each side's length.
return:
The function will return the sum of the area and square of the perimeter of the regular polygon, rounded to 4 decimal places.
'''
    import math
    area=(0.25*n*(s*s))/(math.tan(math.pi/n))
    perimeter=n*s
    return round(area + perimeter**2,4)