n=int(input())
a=1
s=""

while a**3 <= n:
    s=s+str(a**3)+" "
    a=a+1
print(s)
