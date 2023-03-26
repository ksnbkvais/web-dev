n=int(input())
l=list(map(int, input().split()))

i=1
k=0
while i<n-1:
    if l[i]>l[i-1]:k+=1
    i+=1
print(k)
