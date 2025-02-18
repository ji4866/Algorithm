money = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
count = 0

for m in money:
    count += n // m
    n %= m

print(count)