for p in range(int(input())):
    n=list(input())
    e=[int(i) for i in n if int(i)%2==0]
    o=[int(i) for i in n if int(i)%2!=0]
    t=[]
    i,j=0,0
    while i<len(e) and j<len(o):
        if e[i]<o[j]:
            t.append(e[i])
            i+=1
        else:
            t.append(o[j])
            j+=1
    t.extend(e[i:])
    t.extend(o[j:])
    print("".join(map(str, t)))
