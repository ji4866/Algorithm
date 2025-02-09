n = int(input())
p = list(map(int, input().split(' ')))

p.sort()
answer = 0

for i in range(len(p)):
    pre = sum(p[:i+1])
    answer += pre
    
print(answer)