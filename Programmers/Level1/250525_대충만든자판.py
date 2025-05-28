# https://school.programmers.co.kr/learn/courses/30/lessons/160586
from calendar import prmonth
from multiprocessing.connection import answer_challenge


def divide(keymap, target_earch):
    result = []
    for t in target_earch:

        count_compare = []
        for kp in keymap:  # 키맵
            if kp.find(t) != -1:
                save_count = kp.find(t)
                count_compare.append(save_count + 1)

        if count_compare:
            result.append(min(count_compare))
    return result


def solution(keymap, targets):
    answer = []
    for target in targets:
        answer.append(sum(divide(keymap, target)))

    if not any([int(n) for n in answer]):
        return [-1]

    return answer


if __name__ == '__main__':
    # Case1
    # keymap = ["ABACD", "BCEFD"]
    # targets = ["ABCD", "AABB"]

    # Case2
    # keymap = ["AA"]
    # targets = ["B"]

    # Case3
    # keymap = ["AGZ", "BSSS"]
    # targets = ["ASA", "BGZ"]

    # Case4
    keymap = ["A"]
    targets = ["B", "B"]
    print(solution(keymap, targets))
