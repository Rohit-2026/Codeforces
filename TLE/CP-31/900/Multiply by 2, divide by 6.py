for i in range(int(input())):
    n=int(input())
    t=0
    k=n
    c=0
    p=n
    while n%3==0:
        n=n//3
        t+=1
    while k%2==0:
        k=k//2
        c+=1
    if t==c and 6**t==p:
        print(t)
    elif t>c and 6**t==p*2**(t-c):
        print(2*t-c)        
    else:
        print(-1)    