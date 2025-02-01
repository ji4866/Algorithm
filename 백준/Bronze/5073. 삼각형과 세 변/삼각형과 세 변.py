while True:
    a, b, c = map(int, input().split(' '))
    list_ = sorted([a,b,c])

    if a == b == c:
        if a == 0 : break
        print('Equilateral')
    elif sum(list_[:2]) <= list_[-1]: print('Invalid')
    elif a==b or b==c or a==c : print('Isosceles')
    else : print('Scalene')

