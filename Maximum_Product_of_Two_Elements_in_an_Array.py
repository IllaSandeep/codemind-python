a=list(map(int,input().split()))
n=len(a)
a=sorted(a)
print((a[n-1]-1)*(a[n-2]-1))
        