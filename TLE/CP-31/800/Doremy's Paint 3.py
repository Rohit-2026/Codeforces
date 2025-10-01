for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))>2:
        print("No")
    else:
        t=list(set(a))
        if len(t)==1:
            print("Yes")
        elif n%2==0:
            if a.count(t[0])==a.count(t[1]):
                print("Yes")
            else:
                print("No")
        else:
            if a.count(t[0])==a.count(t[1])+1 or a.count(t[0])+1==a.count(t[1]):
                print("Yes")
            else:
                print("No")                    
