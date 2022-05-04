n=int(input())
length=len(str(n))
temp=n
i=0
s=0
while temp>0:
    i=temp%10
    s=s+int(i**length)
    temp=temp//10
    length=length-1
if s==n:
    print(True)
else:
    print(False)