# https://www.acmicpc.net/problem/3085
# level : 2
# tag: brute-force

""" Description
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다.

빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
"""

lst = [
    "CCP",
    "CCP",
    "PPC",
]

# N = input().splitlines()[0] # 3
N = 3
# board = [list(input() for _ in range(N))]
board = [list(s) for s in lst]

ans = 1


def search():
    global ans  # 현재까지 발견한 최대 연속 사탕 개수를 저장할 전역 변수
    # 행을 검사하여 가장 긴 연속된 사탕을 찾는 부분
    for i in range(N):
        cnt = 1  # 현재 연속된 사탕의 개수, 처음은 1로 시작
        for j in range(1, N):  # 두 번째 열부터 시작하여 이전 열과 비교
            if board[i][j - 1] == board[i][j]:  # 이전 칸과 같은 색의 사탕이면
                cnt += 1  # 연속된 사탕 수 증가
                ans = max(ans, cnt)  # 최대값 갱신
            else:
                cnt = 1  # 연속이 끊기면 다시 1로 초기화

    # 열을 검사하여 가장 긴 연속된 사탕을 찾는 부분
    for j in range(N):
        cnt = 1  # 현재 연속된 사탕의 개수, 처음은 1로 시작
        for i in range(1, N):  # 두 번째 행부터 시작하여 이전 행과 비교
            if board[i - 1][j] == board[i][j]:  # 이전 칸과 같은 색의 사탕이면
                cnt += 1  # 연속된 사탕 수 증가
                ans = max(ans, cnt)  # 최대값 갱신
            else:
                cnt = 1  # 연속이 끊기면 다시 1로 초기화


# 인접한 두 사탕을 교환하고, 교환 후 최대 연속 사탕의 개수를 찾는 부분
for i in range(N):
    for j in range(N):
        # 가로로 인접한 사탕을 교환하는 경우
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 교환
            search()  # 교환 후 최대 연속 사탕 개수 탐색
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원상복구

# 여기에 세로로 인접한 사탕 교환 코드를 추가해야 완성됩니다.
