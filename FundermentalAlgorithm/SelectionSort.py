arr = [1, 3, 2, 5 ,4]

for idx, value in enumerate(arr):
    # 최소값은 시작 인덱스로 초기화
    current_idx = idx

    # 선택정렬 조건: 최소값이 있어야함 (오름차순)
    for _id in range(0, len(arr)):
        if arr[_id] < arr[current_idx]:
            arr[_id], arr[idx] = arr[idx], arr[_id]

    # 선택정렬 (내림차순)
    # for _id in range(0, len(arr)):
    #     if arr[_id] > arr[current_idx]:
    #         arr[_id], arr[idx] = arr[idx], arr[_id]

print(arr)
