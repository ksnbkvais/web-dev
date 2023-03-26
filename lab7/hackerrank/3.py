"""
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird"""
a=int(input())
if a%2!=0:print("Weird")
elif a%2==0 and 2<=a and a<=5:print("Not Weird")
elif a%2==0 and 6<=a and a<=20:print("Weird")
elif a%2==0 and a>20:print("Not Weird")