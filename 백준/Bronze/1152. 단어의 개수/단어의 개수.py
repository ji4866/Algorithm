n = input()
a = n.split(' ')
count = 0

for i in a:
    if i == '':
        continue
    else:
        count += 1
print(count)