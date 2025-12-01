#display the even digits of a number

n=int(input("enter a number: "))
while n>0:
    rem=n%10
    n=n//10
    if rem%2==0:
        print(rem)
