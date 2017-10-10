def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b) # 在这个函数中，两种情况都需要返回值  否则没有输出
        

