t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        l.extend(a)
    l.sort()
    le=len(l)
    print(l[le//2])