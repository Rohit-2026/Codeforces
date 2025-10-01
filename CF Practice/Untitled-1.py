def find_Min_Difference(L,P):
    L.sort()
    i=0
    t=100000000
    for i in range(P-1,len(L)):
        t=min(t,L[i]-L[i-P+1])
    return t    
        
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))