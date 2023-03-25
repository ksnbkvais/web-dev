x=0
a=int(input())

while a>0:
    x*=10
    x+=(a%10)
    a=a//10
   
    
print(x)