n=int(input())
a=list(map(int,input().split()))
x=int(input())
l=[]
for i in range(n):
    if a[i]==x:
        l.append(i)
if l==[]:
    print(-1,-1)
else:
    print(min(l),max(l))
