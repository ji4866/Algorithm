def solution(a, b):
    answer = [a[i]*b[i] for i in range(len(a))]
    return sum(answer)