#count the number of digits in a number......................

'''n=int(input("enter a number: "))
count=len(str(n))
print("no of digits are", count)'''



#armstrong no...............................

n=int(input("enter a number: "))
temp=n
count=len(str(n))
sum=0

while n>0:
    rem=n%10
    sum=sum+rem**count
    n=n//10
if sum==temp:
    print("it is an armstrong no")
else:
    print("it is not an armstrong no")