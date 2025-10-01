for i in range(int(input())):
    n=int(input())
    t=[]
    for i in range(1,n+1):
        t.append(2**i)
    t0=t[-1]+sum(t[0:n//2-1])
    t1=sum(t)-t0
    print(abs(t1-t0))
    
            
