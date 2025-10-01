import sys
n=int(input())
sys.stdout.flush()
t=[0]*n
c=0
print("?",1,n)
a=int(input())
sys.stdout.flush()
print("?",2,n)
b=int(input())
sys.stdout.flush()
t[0]=a-b
for i in range(1,n-1):
    print("?",i,i+1)
    c=int(input())
    sys.stdout.flush()
    t[i]=c-t[i-1]
t[-1]=a-sum(t)
print("!",*t)     
sys.stdout.flush()   