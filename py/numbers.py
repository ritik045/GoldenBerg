#display digits of a number

n=int(input("enter a number: "))

while n>0:
    rem=n%10
    print(rem)
    n=n//10