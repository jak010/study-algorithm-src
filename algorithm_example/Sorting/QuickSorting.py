""" Quick Sorting

Author:
    jaka010
Date:
    2022.01.26
Desc:
    - 대표적인 분할 정복 알고리즘을 사용함
    - 특정한 값을 기준으로 큰 숫자와 작은 숫자를 나눈다
    - 피벗(pivot)값을 기준으로 정렬을 진행
    - 시간 복잡도(평균): O(N*logN)
Example:
    - 3 7 8 1 5 9 6 10 2 4 : 피벗 값을 설정 (임의의 기준값, 가운데로 설정해도..)
                             : 왼쪽에서 오른쪽으로 이동할 때는 피벗보다 큰 값을
                             : 오른쪽에서 왼쪽으로 이동할 떄는 피벗보다 작은 값을
                             : 엇갈린 경우 작은 값을 피벗 값의 위치를 바꾼 뒤, 가장 앞의 값을 피벗으로 설정함
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start

    left = start + 1  # 1
    right = end  # 9

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        print(left, right)

    # quick_sort(array, start, right - 1)
    # quick_sort(array, right + 1, end)


if __name__ == '__main__':
    quick_sort(array, start=0, end=len(array) - 1)
    print(array)
