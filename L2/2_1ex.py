iteration = 0
# _1 count = 0
'''
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    count = 0
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
'''
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
