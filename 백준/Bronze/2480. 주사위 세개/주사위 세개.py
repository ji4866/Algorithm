# 주사위 3개
a, b, c = list(map(int, input().split()))

if a == b == c:
  money = 10_000 + a * 1_000

elif a == b or a == c or b == c:
  if a == b or a == c:
    money = 1_000 + a*100
  else:
    money = 1_000 + b*100

else:
  money = max(a,b,c)*100
print(money)