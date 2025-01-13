def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum_ = 0

    for i in range(len(A)):
        sum_ += A[i]*B[i]
    return sum_