a,b=map(int,input().split())
l=list(map(int,input().split()))
if(b not in l):
    print(-1)
else:
    print(l.index(b))