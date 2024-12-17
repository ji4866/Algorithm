hour, minute = list(map(int, input().split())) # 종료되는 시각의 시와 분
cook = int(input()) # 요리하는 데 필요한 시간

minute = minute + cook

hour += (minute//60)
minute = minute%60

if hour>23:
  hour = hour-24


print(hour, minute)