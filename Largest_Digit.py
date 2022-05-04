n=int(input())
i=0
lar=0
while n>0:
    i=n%10
    if lar<i:
        lar=i
    n=n//10
print(lar)