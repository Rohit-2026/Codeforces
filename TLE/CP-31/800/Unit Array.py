for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=0
    if sum(a)<0:
        t+=abs(sum(a))
        if t%2!=0:
            t=(t//2)+1
        else:
            t=t//2    
        if (a.count(-1)-t)%2==1:
            t+=1
            print(t)
        else:
            print(t)
    else:
        if a.count(-1)%2==0:
            print(0)
        else:
            print(1)    



        
