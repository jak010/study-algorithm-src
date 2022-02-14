""" Insertion Sorting

Author:
    jaka010
Date:
    2021.06.05(sat)
Desc:
    정렬 범위를 확장해나가면서 정렬을 진행
    이미 정렬된 배열 부분과 확장된 범위 부분을 비교하며
    자신의 위치를 찾아 삽입
"""

arr = [2, 5, 3, 1, 4]
# 2 5 3 1 4

# Insertion Sorting Code Example
# for end in range(1, len(arr)):
#     for i in range(end, 0, -1):
#         if arr[i - 1] > arr[i]:
#             arr[i], arr[i - 1] = arr[i - 1], arr[i]

for idx in range(len(arr)):
    for point in range(idx, 0, -1):
        if arr[point] > arr[point - 1]:
            arr[point], arr[point - 1] = arr[point - 1], arr[point]

print(arr)
