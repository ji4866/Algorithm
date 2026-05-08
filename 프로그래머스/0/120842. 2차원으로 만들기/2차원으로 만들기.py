def solution(num_list, n):
    num = []
    answer = []

    for i in range(len(num_list)):
        num.append(num_list[i])
        if (i+1)%n == 0:
            answer.append(num)
            num = []
            
    return answer