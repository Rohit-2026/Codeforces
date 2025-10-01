for i in range(int(input())):
    s=input()
    t=[]
    i=0
    c=0
    while i<len(s):
        if not t:
            t.append(s[i])
        else:
            if t[-1]!=s[i]:
                t.pop()
                c+=1
            else:
                t.append(s[i])
        i+=1
    if c%2==1:
        print("DA")
    else:
        print("NET")                     


