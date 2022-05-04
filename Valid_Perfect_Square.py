import math
n=int(input())
while n:
    x=int(input())
    r=math.sqrt(x)
    if int(r+0.5)**2==x:
        print('True')
    else:
        print('False')
    n-=1