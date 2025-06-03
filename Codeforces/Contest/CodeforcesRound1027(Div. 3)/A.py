from math import sqrt
t=int(input())
for _ in range(t):
    s=int(input())
    x=round(sqrt(s)//2)
    test=False
    for i in range(x,round(sqrt(s))+1):
        for j in range(x,-1,-1):
            if (i+j)**2==s:
                test=True
                break
            
    
    if test==True:
        l=[j,i]
        print(*l)
    else:
        print(-1)