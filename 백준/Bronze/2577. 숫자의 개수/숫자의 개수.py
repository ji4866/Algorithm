A = int(input())
B = int(input())
C = int(input())

str_ = str(A * B * C)
count_list = [0,0,0,0,0,0,0,0,0,0]

for st in str_:
    count_list[int(st)] += 1

for i in count_list:
    print(i)