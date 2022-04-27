a=int(input())
n=1
c=1
while n*n<=a:
    if a==n*n:
        print('True')
        c=0
        break
    n+=1
if c!=0:
    print('False')
    
        

