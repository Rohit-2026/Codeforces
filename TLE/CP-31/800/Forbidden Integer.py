for i in range(int(input())):
    n,k,x=map(int,input().split())
    if x!=1:
        print("YES")
        print(n)
        print(*n*[1])
    else:
        if n%2==0 and k>=2:
            print("YES")
            print(n//2)
            print(*n//2*[2])
        elif n%2==1 and k>=3:
            print("YES")
            print(((n-3)//2)+1)
            if (n-3)//2<=0:
                print(3)
            else:
                print(3,*(n-3)//2*[2])
        else:
            print("NO")            


