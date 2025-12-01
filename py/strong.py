'''n=int(input("enter a number: "))
while n>0:
    rem=n%10'''

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