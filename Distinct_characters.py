a=input()
c=0
for i in range(0,26):
    if chr(97+i) in a:
        print(chr(97+i),end='')