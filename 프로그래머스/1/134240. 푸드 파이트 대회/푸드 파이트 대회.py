def solution(food):
    p1, p2, water, count = [], [], '0', 1
    
    for f in food[1:]:
        for i in range(f//2):
            p1.append(str(count))
            p2.append(str(count))
        count += 1
        
    p2 = p2[::-1]

    return ''.join(p1) + water + ''.join(p2)