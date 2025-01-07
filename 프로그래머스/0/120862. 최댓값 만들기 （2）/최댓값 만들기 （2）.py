def solution(numbers):
    numbers = sorted(numbers)
    max_1 = numbers[-1]*numbers[-2]
    max_2 = numbers[0]*numbers[1]

    if max_1>=max_2:return max_1
    else:return max_2