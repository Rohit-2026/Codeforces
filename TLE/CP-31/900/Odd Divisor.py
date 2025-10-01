for i in range(int(input())):
    n=str(bin(int(input())))
    if n.count("1")==1:
        print("NO")
    else:
        print("YES")    
