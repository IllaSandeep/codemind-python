n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
if n==m:
    for i in range(0,n):
        if a[i] not  in b:
            print('False')
            break
    else:
        print('True')
else:
    print('True')
            