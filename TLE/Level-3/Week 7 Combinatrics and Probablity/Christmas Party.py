n=int(input())
t=[0,0,1,2]
m=(10**9)+7
if n in [0,1,2,3]:
    print(t[n])
else:
    for i in range(4,n+1):
        t.append(((i-1)*(t[-1]+t[-2]))%m)
    print(t[-1])    