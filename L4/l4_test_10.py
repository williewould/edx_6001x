def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)<=1:
        return aStr==char
    # 注意字符串引用用[]  注意整除 // 防止浮点数引用的出现
    elif char<aStr[len(aStr)//2]:
        return isIn(char,aStr[:len(aStr)//2])
    else:
        return isIn(char,aStr[len(aStr)//2:])
