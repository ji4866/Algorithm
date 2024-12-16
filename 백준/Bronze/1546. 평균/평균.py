n = int(input()) # 과목 개수
score_list = list(map(int, input().split())) # 성적 점수 리스트
m = max(score_list)
new_score_list= list(map(lambda x:x/m*100, score_list))
avg = sum(new_score_list)/len(new_score_list)
print(avg)