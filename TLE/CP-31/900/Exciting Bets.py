for i in range(int(input())):
    n,k=map(int,input().split())
    t=abs(n-k)
    if t==0:
        print(0,0) 
    else: 
        print(t,min(n%t,t-n%t))
