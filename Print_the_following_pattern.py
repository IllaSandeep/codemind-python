n=int(input())
l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end='')
    for j in range(i+1):
        print(l[j],end='')
    for j in range(i-1,-1,-1):
        print(l[j],end='')
    print()
    
    