for i in range(int(input())):
    n=int(input())
    a=input()
    i=0
    j=n-1
    while i<j:
        if a[i]!=a[j]:
            i+=1
            j-=1
        else:
            break
    print(j-i+1)        
