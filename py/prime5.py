#display prime digits of a number

n=int(input("enter a number: "))
while n>0:
    rem=n%10
    if rem==2 or rem==3 or rem==5 or rem==7:
        print(rem)
    n=n//10