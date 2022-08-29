def lcm(a,b):
    maxi=max(a,b)
    while True:
        if maxi%a==0 and maxi%b==0:
            break
        else:
            maxi+=max(a,b)
    return maxi
n=int(input())
a=list(map(int,input().split()))
l=lcm(a[0],a[1])
for i in range(2,n):
    l=lcm(l,a[i])
print(l)