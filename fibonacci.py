n1=0
n2=1
num=int(input())
print("0 1",end=' ')
for i in range(2,num,1):
     n3=n1+n2
     print(n3,end=' ')
     n1=n2    
     n2=n3    