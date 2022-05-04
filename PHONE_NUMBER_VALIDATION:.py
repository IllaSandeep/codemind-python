n=int(input())
i=0
c=0
while n!=0:
    c+=1
    n=n//10
if c==10:
    print('Valid')
else:
    print('Invalid')