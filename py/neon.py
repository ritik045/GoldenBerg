n=int(input("enter a number: "))
sq=n*n
sum=0
while sq>0:
    rem=sq%10
    sum=sum+rem
    sq=sq//10

if (sum==n):
    print("this is a neon number")
else:
    print("not a neon number")

