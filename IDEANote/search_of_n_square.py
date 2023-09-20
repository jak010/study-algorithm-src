arr = [1, 2, 3, 4, 1]


def search_of_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return i, j


def linear_search_of_duplicate(arr):
    seen = set()
    duplicates = []

    for i, num in enumerate(arr):
        if num in seen:
            duplicates.append(i)
        else:
            seen.add(num)
    return duplicates

# 예시 호출
arr = [1, 2, 3, 4, 1]
result = linear_search_of_duplicate(arr)
print(result)  # 출력: [4]
