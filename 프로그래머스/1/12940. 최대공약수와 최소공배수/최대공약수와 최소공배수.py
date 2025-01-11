def solution(n, m):
    answer = []
    n_list = [i for i in range(1, n+1) if n%i == 0]
    m_list = [i for i in range(1, m+1) if m%i == 0]
    
    # 최대 공약수
    a = [i for i in n_list for j in m_list if i == j]
    answer.append(a[-1])
    
    # 최소 공배수
    i = max(n,m)
    
    while True:
        if i%n == 0 and i%m==0:
            answer.append(i)
            break
        i+= 1
        
    return answer