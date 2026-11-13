x=int(input())
k=0
for a in range(1,int(x**0.5)+1):
    for b in range(a,int(x**0.5)+1):
        if a*a+b*b==x:
            k+=1
print(k)
