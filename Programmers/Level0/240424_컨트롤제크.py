def solution(s):
    lst = s.split(" ")

    count = 0
    current = 0
    for e in lst:
        if e != 'Z':
            count += int(e)
            current = int(e)
        if e == "Z":
            count -= current

    return count


if __name__ == '__main__':
    print(solution("1 2 Z 3"))
    print(solution("10 20 30 40"))
