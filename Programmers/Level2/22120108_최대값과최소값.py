from typing import Tuple, List


def solution(s):
    split_of_space = [int(x) for x in s.split(" ")]

    return f"{min(split_of_space)} {max(split_of_space)} "


def solution2(s):
    s = list(map(int, s.split()))
    s.sort()

    return f"{s[0]} {s[-1]}"


def solution3(s):
    space_index = []
    str_length = len(s)

    for index, ch in enumerate(s):
        if ch.isspace():
            space_index.append(index)

    space_index.insert(0, 0)
    space_index.append(str_length)

    offset_range: List[Tuple[int, int]] = []
    for index in range(len(space_index)):
        if index == 0:
            continue

        offset_range.append((space_index[index - 1], space_index[index]))

    answer_result = []
    for offset in offset_range:
        result = int(s[offset[0]: offset[1]].strip())
        answer_result.append(result)

    return f"{min(answer_result)} {max(answer_result)}"


if __name__ == '__main__':
    # strs = "1 2 3 4"
    strs = "-1 -2 -3 -4"
    # print(len(strs))
    s = solution3(strs)

    print(s)
