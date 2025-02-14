sum_ = 0
n = int(input())

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a.sort()
b.sort(reverse = True)

for i in range(n):
    sum_ += a[i]*b[i]
    
print(sum_)