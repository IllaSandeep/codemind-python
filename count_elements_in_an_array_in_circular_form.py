x=int(input())
a=list(map(int,input().split()))
c=0
if (a[x-2]%2==0 and a[0]%2!=0) or (a[x-2]%2!=0 and a[0]%2==0):
    c+=1
if (a[1]%2==0 and a[x-1]%2!=0) or (a[1]%2!=0 and a[x-1]%2==0):
    c+=1
for i in range(1,x-1):
    if a[i-1]%2==0 and a[i+1]%2!=0 or a[i-1]%2!=0 and a[i+1]%2==0:
        c+=1
print(c)