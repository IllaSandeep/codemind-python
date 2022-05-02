a=int(input())
for i in range(a):
    for j in range(a):
        if i==j or i-j==a+1:
            print('0',end='')
        else:
            print('x',end='')
    print()