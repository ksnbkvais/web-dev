x=input()
y=0
for i in range(len(x)):
    y+=int(x[i])*(2**(len(x)-i-1))
print(y)
