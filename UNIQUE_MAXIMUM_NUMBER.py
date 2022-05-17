n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in range(n):
    for j in range(n):
        if(a[i]==a[j]):
            c+=1
    if c==1:
        l.append(a[i])
    c=0
if len(l)==0:
    print('-1')
elif l!=0:
    print(max(l))