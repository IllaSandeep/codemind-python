import math
n=int(input())
no=len(str(n))
sq=n**2
las=sq%pow(10,no)
if las==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    