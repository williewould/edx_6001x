def biggest(aDict):
    '''
    aDict: A dictionary, where all the v
alues are lists.
    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    mx = list(aDict.keys())[0]
    for i in aDict:
        if len(aDict[mx]) < len(aDict[i]):
            mx = i
    return mx
################
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))
