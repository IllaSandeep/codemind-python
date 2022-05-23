n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i==n+1-j:
            print(n-i+1,end=' ')
        else:
            print(' ',end='')
    print()
