"""
Date: 2021.12.20
첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
"""
time = input()
hour, minute = time.split()
hour = int(hour)
minute = int(minute)

MINUS_NUMBER = 45

# 입력된 minute이 MINUS_NUMBER 보다 작다면 무조건 HOURS를 뺸다
if minute - MINUS_NUMBER < 0:
    hour = hour - 1  # 분이 음수 값이 되서 시간은 입력한 시간에서 -1이 됨
    minute = 60 + (minute - MINUS_NUMBER)  # minute 뺴주기

else:
    minute -= MINUS_NUMBER

if hour < 0:
    hour = 23

print(str(hour), str(minute))
