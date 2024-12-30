def solution(n):
    answer = 0

    for a in range(1, n+1):
        b = n//a
        if a*b == n:
            answer += 1

    return answer