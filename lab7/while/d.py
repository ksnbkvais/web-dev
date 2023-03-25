a=int(input())
i=0
k=0
while i<a:
    if 2**i==a:k=1
    i+=1
if k==1:print("YES")
else:print("NO")