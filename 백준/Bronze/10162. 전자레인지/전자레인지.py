t = int(input())
buttons = [300, 60, 10]

if t% buttons[-1] != 0:
    print(-1)
else:
    for b in buttons:
        count = t//b
        t %= b
        print(count, end= ' ')