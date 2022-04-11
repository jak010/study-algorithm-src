# 공간 복잡도 O(1)
# 시간 복잡도 O(n^2)
# - 모든 인덱스에 접근해야하기 때문에 기본 O(N) + 다른 하나의 루프에서 인덱스 비교를 위한 O(n)

arr = [4, 1, 2, 5, 3]

for idx1 in range(len(arr) - 1):

    for idx2 in range(idx1, len(arr)):  # idx1이 증가함에 따라 idx2 범위 좁히기

        if arr[idx1] < arr[idx2]:  # 최소 값은 arr[idx_1] 이라고 가정 (내림차순)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

print(arr)

arr = [4, 1, 2, 5, 3]
for idx, value in enumerate(arr):
    # 최소값은 시작 인덱스로 초기화
    current_idx = idx

    # 선택정렬 조건: 최소값이 있어야함 (오름차순)
    for _id in range(0, len(arr)):
        if arr[_id] < arr[current_idx]:
            arr[_id], arr[idx] = arr[idx], arr[_id]
#
#     # 선택정렬 (내림차순)
#     # for _id in range(0, len(arr)):
#     #     if arr[_id] > arr[current_idx]:
#     #         arr[_id], arr[idx] = arr[idx], arr[_id]
#
print(arr)
