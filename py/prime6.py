#sum of prime digits of a number

n=int(input("enter a number: "))
sum=0
while n>0:
    rem=n%10
    if rem==2 or rem==3 or rem==5 or rem==7:
        print(rem)
        sum=rem+sum
    n=n//10
print("sum of prime numbers are", sum)
