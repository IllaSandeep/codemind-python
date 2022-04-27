n=int(input())
s=0
temp=n
while n!=0:
    i=n%10
    s=s+i
    n=n//10
if temp%s==0:
    print('True')
else:
    print('False')