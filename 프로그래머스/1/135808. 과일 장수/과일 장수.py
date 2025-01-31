def solution(k, m, score):
    answer, box = 0, []
    boxes = len(score)//m
    
    score.sort()
    
    for i in range(boxes):
        box = []
    
        for i in range(m):
            box.append(score[-1])
            score.pop()

        answer += min(box)*m
    
    return answer