n = int(input())
count = n//5
n %= 5
if n == 0:
    print(count)
else:
    while n > 0:
        if n%3 == 0:
            count += n//3
            print(count)
            break
        else:
            count -= 1
            n += 5
            if count < 0:
                print(-1)
                break