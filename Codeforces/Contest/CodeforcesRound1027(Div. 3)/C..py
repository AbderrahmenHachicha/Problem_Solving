t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    
    t=[l[0]]
    h=l[1:]
    for i in h:
        if i>=t[-1]+2:
            t.append(i)
    
 
    print(len(t))