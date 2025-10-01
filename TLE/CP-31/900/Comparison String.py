for i in range(int(input())):
    n=int(input())
    a=input()
    c=1
    m=0
    for i in range(1,n):
        if a[i]==a[i-1]:
            c+=1
        else:
            c=1
        m=max(m,c)
    if n==1:
        print(2)
        continue    
    print(m+1)            