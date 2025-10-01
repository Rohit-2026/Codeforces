x= int(input())
t=0
for i in range(1,10):
    for j in range(1,10):
        if i*j!=x:
            t+=i*j
print(t)
