n=int(input())
a=list(map(int,input().split()))
if n%2==0:
    for i in range(n):
        print(a[i],end=' ')
elif n%2!=0:
    for i in range(n):
        print(a[i],end=' ')
    print('0')