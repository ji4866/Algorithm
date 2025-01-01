def solution(myString):
    answer = []
    
    while True:
        index = myString.find('x')
        if index == -1:
            answer.append(len(myString))
            return answer
        answer.append(len(myString[:index]))
        myString = myString[index+1:] # 다음 문자열
        
    return answer