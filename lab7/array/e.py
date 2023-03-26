n=int(input())
l=list(map(int, input().split()))

i=1
k=0
while i<n-1:
    if l[i]>=0 and l[i-1]>=0:k=1
    elif l[i]<0 and l[i-1]<0:k=1
    
    i+=1
if k==1:print("YES")
else:print("NO")