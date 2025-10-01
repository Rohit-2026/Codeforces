for i in range(int(input())):
    a,b=input().split()
    j=len(b)-1
    i=len(a)-1
    while i>=0 and j>=0:
        if a[i]==b[j]:
            i-=1
            j-=1
        else:
            i-=1
    if j==-1 and len(set(a[i+1:]))==len(a)-i:
        print("YES")
    else:
        print("NO")            
               