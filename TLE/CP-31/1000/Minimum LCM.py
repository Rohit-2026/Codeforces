for i in range(int(input())):
    n=int(input())
    c=n-1
    t=0

    for i in range(2,int(n**0.5)+1):
        if (n-i)%i==0:
            if c>n-i:
                t=n-i
                c=n-i
    if n-t>n-1:
        print(1,n-1)
    else:
        print(n-t,t)           
