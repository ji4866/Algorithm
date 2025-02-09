n, k = map(int, input().split(' '))
coin = [int(input()) for i in range(n)]
coin.sort(reverse = True)
count = 0

for c in coin:
    if c <= k:
        count += k//c
        k %= c
    if k == 0 : break
        
print(count) 