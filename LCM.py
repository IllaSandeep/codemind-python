a,b=map(int,input().split())
max=max(a,b)
while True:
    if max%a==0 and max%b==0:
        print(max)
        break
    max+=1