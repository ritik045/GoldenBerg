
'''x=int(input("enter a number: "))
factorial=1

for i in range(1,x+1):
    factorial=factorial*i
    
print("the factorial of the number is", factorial)'''


#strong number



'''


x=int(input("enter a number: "))
temp=x
fact=1
sum=0

while x>0:
    rem=x%10
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    x=x//10
if(sum==temp):
    print("this is a strong number")
else:
    print("not a strong number")'''

num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    rem = num % 10
    fact = 1
    for i in range(1, rem + 1):
        fact *= i
    sum += fact
    num //= 10

if sum == temp:
    print(temp, "is a Strong Number")
else:
    print(temp, "is not a Strong Number")
