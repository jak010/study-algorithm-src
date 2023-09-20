def number_of_paths(n):
    # 오르는 방법에 관해 하드코딩으로 처리하기
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    return number_of_paths(n - 1) + number_of_paths(n - 2)


print(number_of_paths(9))

