for p in range(int(input())):
    a=[input().strip() for i in range(10)]
    c=0
    for i in range(10):
        for j in range(10):
            if a[i][j]=='X':
                if i==0 or i==9 or j==9 or j==0:
                    c+=1
                elif i==1 or i==8 or j==8 or j==1:
                    c+=2
                elif i==2 or j==2 or j==7 or i==7:
                    c+=3
                elif i==3 or j==6 or i==6 or j==3:
                    c+=4 
                else:
                    c+=5                             
    print(c)
