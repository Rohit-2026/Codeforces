a=[0]*100
for i in range(int(input())):
    m=input().split()
    if m[0]=="1":
        a.append(m[1])
    else:
        print(int(a.pop())) 

