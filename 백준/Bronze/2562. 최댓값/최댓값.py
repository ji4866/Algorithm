numbers = []

for i in range(9):
  n = int(input())
  numbers.append(n)

i = 0
while True:
  if numbers[i] == max(numbers):
    print(max(numbers))
    print(i+1)
    break
  i+= 1
