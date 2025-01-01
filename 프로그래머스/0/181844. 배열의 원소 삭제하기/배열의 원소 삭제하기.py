def solution(arr, delete_list):
    answer = arr.copy()
    for a in arr:
        if a in delete_list:
            answer.remove(a)
    return answer