from itertools import permutations, combinations


def solution(babbling):
    enable = ["aya", "ye", "woo", "ma"]

    enable_combination = []

    for idx in range(0, len(enable) + 1):
        enable_combinations = permutations(enable, idx)

        sep = ''
        for comb in enable_combinations:
            if sep.join(comb):
                enable_combination.append(sep.join(comb))

    enable.extend(enable_combination)

    enable_combination_repeat = [bab * 2 for bab in enable]
    enable.extend(enable_combination_repeat)

    result = 0
    for token in babbling:
        if token in enable:
            result += 1

    return result


def solution2(babbling):
    enables = ["aya", "ye", "woo", "ma"]

    counter = 0
    for babble in babbling:

        for enable in enables:
            babble = babble.replace(enable, " ").strip()
            if len(babble) == 0:
                counter += 1
                break

    return counter


if __name__ == '__main__':
    test_01 = ["aya", "yee", "u", "maa", "wyeoo"]
    test_02 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

    # print(solution(test_02))

    print(solution2(test_02))
    # print(solution2(test_01))
