# Prime Numberscount = 0
count=0
for y in range(20,31):
    for j in range(1,y+1):
        if y % j == 0:
            count += 1
    if count == 2: 
        print(f"{y} is a prime number")
    count = 0