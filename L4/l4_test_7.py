# base^exp
base=2
exp=3
a=1
if exp==0:
    a=1
else:
    for i in range(exp):
        a*=base
        print(a)
