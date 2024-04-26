def solution(before, after):
    b_map = {ch: before.count(ch) for ch in before}
    a_map = {ch: after.count(ch) for ch in after}

    for k, v in a_map.items():
        if k in b_map:
            a_map[k] -= b_map[k]

    for i in list(a_map.values()):
        if i != 0:
            return int(False)

    return int(True)


if __name__ == '__main__':
    print(solution("olleh", "hello"))
    print(solution("allpe", "apple"))
    print(solution("a", "al"))
