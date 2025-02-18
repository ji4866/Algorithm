m = [25, 10, 5, 1]
t = int(input())

for n in range(t):
    count_list = []
    x = int(input())
    
    for i in m:
        count = x // i
        x = round(x%i, 2)
        count_list.append(int(count))

    for c in count_list:
        print(c, end=' ')
        
    print()
