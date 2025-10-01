for i in range(int(input())):
    n=list(input())
    c=0
    while n:
        if n[-1]=="5" or n[-1]=="0":
            break
        c+=1
        n.pop(-1)
    while n:
        if int(n[-2])%2==1 or int(n[-2])==0:
            break
        c+=1
        n.pop(-2)
    print(c)    