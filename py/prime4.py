count = 0
total_sum = 0

for y in range(20, 31):
    for j in range(1, y + 1):
        if y % j == 0:
            count += 1
    if count == 2:
        total_sum += y
    count = 0
print("The sum of the prime numbers is:", total_sum)