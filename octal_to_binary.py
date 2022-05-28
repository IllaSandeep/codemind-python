n=int(input())
i=0
sum=0
while(n!=0):
    s=n%10
    sum=sum+(s)*(8**i)
    n=n//10
    i+=1
print ("{0:b}".format(sum))