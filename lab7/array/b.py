n=int(input())
l=list(map(int, input().split()))

i=0
while i<n-1:
    if l[i]%2==0:print(l[i],end=" ")
    i+=1
    