n=int(input())
l=list(map(int, input().split()))

i=0
k=0
while i<n-1:
    if l[i]>0:k+=1
    i+=1
print(k)