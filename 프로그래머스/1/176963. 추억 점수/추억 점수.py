def solution(name, yearning, photo):
    answer = []

    for ph in photo:
        ph_sum = 0

        for p in ph:
            if p in name:
                p_index = name.index(p)
                ph_sum += yearning[p_index]

        answer.append(ph_sum)
        
    return answer