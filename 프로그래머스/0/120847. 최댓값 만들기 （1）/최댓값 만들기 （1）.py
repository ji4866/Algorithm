def solution(numbers):
    answer = 1
    for i in range(2):
        answer *= max(numbers)
        numbers.remove(max(numbers))
        
    return answer