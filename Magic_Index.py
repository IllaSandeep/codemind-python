for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=0
    for i in range(n):
        if a[i]==i:
            f=1
            print(a[i])
            break
    if f==0:
        print(-1)
    