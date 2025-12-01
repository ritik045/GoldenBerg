
n=int(input("enter a number: "))
temp=n
sum=0
product=1
total_sum=0

while n>0:
    rem=n%10
    sum=sum+rem
    product=product*rem
    total_sum=sum+product
    n=n//10
    
if temp==total_sum:
    print("special digit")
else:
    print("not special digit")
