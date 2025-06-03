n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(len(l)):
    if l[i]%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
        
 
if len(odd)==1:
    x=l.index(odd[0])+1
    
elif len(even)==1:
    x=l.index(even[0])+1
    
print(x)