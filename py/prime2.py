
for x in range(20,31):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1

if(count==2):
    print('is a prime no')
else:
    print('not a prime no')