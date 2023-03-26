"""
Given list is 2 3 6 6 5 . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""
a=int(input())
k=[]
for i in range (a):
    k.append(int(input()))
max=k[0]
for i in range (len(k)-1):
    if max<k[i]:
        max=k[i]
k.sort()
for i in range (len(k)-1):
    if max==k[i]:
        k.pop(i)

print(k[len(k)-1])