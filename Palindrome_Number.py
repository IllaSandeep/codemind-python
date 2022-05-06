x=int(input())
for i in range(x):
    s=int(input())
    rev=0
    n=s
    while n:
        i=n%10
        rev=rev*10+i
        n=n//10
    if rev==s:
        print(True)
    else:
        print(False)