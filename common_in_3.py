for _ in range(int(input())):
    n,m,o=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    l=[]
    for i in a:
        if i in b:
            l.append(i)
    f=0
    for i in set(c):
        if i in l:
            f=1
            print(i,end=' ')
    if f==0:
        print(-1,end=' ')
    print()