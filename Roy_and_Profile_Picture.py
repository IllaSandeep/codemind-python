L=int(input())
N=int(input())
for i in range(0,N):
    W,H=map(int,input().split())
    if W<L or H<L:
        print("UPLOAD ANOTHER")
    elif W==H:
        print("ACCEPTED")
    elif W==L and H==L:
        print("ACCEPTED")
    elif W>L or H>L:
        print("CROP IT")