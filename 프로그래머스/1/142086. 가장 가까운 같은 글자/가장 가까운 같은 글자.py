def solution(s):
    a, s_list = [], []

    for i in s:
        if i not in s_list:
            a.append(-1)
        else:
            for j in range(len(s_list)-1, -1, -1):
                if s_list[j] == i:
                    a.append(len(s_list) - j)
                    break

        s_list.append(i)
    return a