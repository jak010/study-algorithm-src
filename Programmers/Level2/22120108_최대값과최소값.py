def solution(s):
    split_of_space = [int(x) for x in s.split(" ")]

    return f"{min(split_of_space)} {max(split_of_space)} "


def solution2(s):
    s = list(map(int, s.split()))
    s.sort()

    return f"{s[0]} {s[-1]}"


if __name__ == '__main__':
    strs = "1 2 3 4"
    s = solution2(strs)

    print(s)
