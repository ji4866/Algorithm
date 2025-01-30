def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    p1_count, p2_count, p3_count = 0, 0, 0
    p1_len, p2_len, p3_len = len(p1), len(p2), len(p3)
    
    for i in range(len(answers)):
        if answers[i] == p1[i%p1_len]:p1_count += 1
        if answers[i] == p2[i%p2_len]:p2_count += 1
        if answers[i] == p3[i%p3_len]:p3_count += 1

    count_ =  [p1_count, p2_count, p3_count]
    max_ = max(p1_count, p2_count, p3_count)
    answer = [i+1 for i in range(3) if count_[i] == max_]
    
    return answer