import sys
t=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,49,16,25,9,4]
c=0
for i in t:
    print(i)
    sys.stdout.flush()
    n=input()
    if n=="yes":
        c+=1
if c>1:
    print("composite")
else:
    print("prime")
