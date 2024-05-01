def solution(arr):
    latest = arr
    count = 0
    for _ in range(len(arr)):
        _temp = []
        for idx, value in enumerate(latest):

            if value >= 50 and value % 2 == 0:
                t = value / 2
            elif value < 50 and value % 2 != 0:
                t = (value * 2) + 1
            else:
                t = value

            _temp.append(int(t))

        if latest != _temp:
            latest = _temp
            count += 1
        else:
            break

    return count


if __name__ == '__main__':
    print(solution(arr=[1, 2, 3, 100, 99, 98]))
