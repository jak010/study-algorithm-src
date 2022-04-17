"""  Bubble sort in Python of Using with Enumerate

Author:
    jak010
Date:
    2021.06.05 (Sat)

Description:
    Time complexity -> O(N^2)

"""

arr = [5, 3, 7, 9, 1]

for i in range(len(arr)):  # 반복 횟수
    for j in range((len(arr) - 1) - i):  # 탐색 범위를 배열의 끝에서부터 -1씩 좁아짐
        if arr[j] > arr[j + 1]:
            print(arr)
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)


# for idx in range(len(arr)):
#     for j in range(len(arr) - 1):
#         if arr[j] < arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
# print(arr)
