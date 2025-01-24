def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        a = array[i-1:j]
        a.sort()
        answer.append(a[k-1])
    return answer