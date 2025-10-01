for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    i=0
    j=0
    t=1000000000
    cb=0
    cw=0
    if k==1:
        if s.count("B")>0:
            print(0)
        else:
            print(1)
        continue
    elif n==k:
        print(s.count("W"))
        continue
    while j<n:
        if j-i<k:
            if s[j]=="B":
                cb+=1
            else:
                cw+=1    
            j+=1     
        else:
            t=min(t,cw)
            if s[i]=="B":
                cb-=1
            else:
                cw-=1    
            i+=1   
    t=min(t,cw)          
    print(t)        


