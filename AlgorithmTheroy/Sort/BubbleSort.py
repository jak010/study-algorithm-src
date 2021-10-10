"""  Bubble sort in Python of Using with Enumerate

Author:
    jak010
Date:
    2021.06.05 (Sat)

Description:
    Time complexity -> O(N^2)

"""

arr = [1, 3, 2, 5, 4]

for idx in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
