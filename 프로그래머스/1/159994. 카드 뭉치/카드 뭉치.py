def solution(cards1, cards2, goal):
    index1, index2 = [], []
    idx1, idx2 = 0,0

    for g in goal:
        if g in cards1 : index1.append(cards1.index(g))
        else : index2.append(cards2.index(g))

    for i in index1:
        if i != idx1 : return 'No'
        idx1 += 1

    for i in index2:
        if i != idx2 : return 'No'
        idx2 += 1

    return 'Yes'