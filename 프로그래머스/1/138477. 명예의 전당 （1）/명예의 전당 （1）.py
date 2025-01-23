def solution(k, score):
    a, answer = [], []

    for s in score:
        a.append(s)
        answer.append(min(a))

        if len(a) > k:
            a.remove(min(a))
            answer[-1] = min(a)
            
    return answer