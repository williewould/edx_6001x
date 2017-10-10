# 求最大公约数
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    i_max=0
    if a<b:
        for i in range(1,a+1):
            if a%i==0 and  b%i==0:
               if i>=2:
                   i_max=i
                
            
    else:
        for i in range(1,b+1):
            if a%i==0 and  b%i==0:
                if i>=2:
                    i_max=i
            
    if i_max==0:
        i_max=1
    return i_max
