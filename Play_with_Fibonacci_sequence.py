def fib(n,s,a,b):
    if n==s:
        return 0
    c=a+b
    b=a
    a=c
    print(c,end=' ')
    return fib((n+1),s,a,b)
x=int(input())
a=0
b=1
print(a,end=' ')
c=a+b
fib(1,x,a,b)