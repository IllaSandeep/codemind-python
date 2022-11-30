def ins(a,m):
    for i in range(len(a)):
        if a[i]>m:
            return i
    return n
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    print(ins(a,m))