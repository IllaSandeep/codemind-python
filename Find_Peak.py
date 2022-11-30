n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
    if a[i-1]<a[i] and a[i]>a[i+1]:
        print(i)
        break