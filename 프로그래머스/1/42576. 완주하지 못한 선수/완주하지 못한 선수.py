def solution(a, b):
    c = dict()

    for i in a:
        if i in c : c[i] += 1
        else : c[i] = 1

    for j in b:
        if j in c:
            c[j] -= 1

    for k, v in c.items():
        if v == 1 : return k