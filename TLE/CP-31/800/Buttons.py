for i in range(int(input())):
    a,b,c=map(int,input().split())
    if c%2==0:
        a+=c//2
        b+=c//2    
    else:
        a+=(c//2)+1
        b+=c//2    
    if a>b:
        print("First")
    else:
        print("Second")    
            