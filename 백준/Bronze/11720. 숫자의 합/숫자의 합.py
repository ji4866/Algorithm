n = int(input())
num = input()
num_list = []

for i in range(len(num)):
    num_list.append(int(num[i]))

print(sum(num_list))