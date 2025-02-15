i = 0

while True:
    i += 1
    l, p, v = map(int, input().split(' '))

    if l == 0 and p == 0 and v == 0:
        break

    count = (v//p)*l
    remain = v%p
    
    if remain >= l:
        count += l
    else: count += remain
        
    print(f'Case {i}: {count}')
    
    