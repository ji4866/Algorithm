def solution(n):
    array = []

    for i in range(n):
        ary = [0 if i != j else 1 for j in range(n)]
        array.append(ary)
    return array