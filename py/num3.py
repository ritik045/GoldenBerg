#sum of the even digits of a number

n=int(input("enter a number: "))
sum=0
while n>0:
    rem=n%10
    n=n//10
    if rem%2==0:
        print(rem)
        sum=sum+rem

print("the sum is", sum)
