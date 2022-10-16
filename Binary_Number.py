n=int(input())
for i in range(2**n):
    b=bin(i)[2:]
    l=len(b)
    x=str(0)*(n-l)+b
    print(x)
    