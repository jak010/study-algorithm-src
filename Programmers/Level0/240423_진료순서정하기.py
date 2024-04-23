# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    hmap = {e: 0 for e in emergency}

    rank = 1
    for e in sorted(emergency, reverse=True):
        hmap[e] = rank
        rank += 1

    return list(hmap.values())


if __name__ == '__main__':
    print(solution([3, 76, 24]))
    print(solution([1, 2, 3, 4, 5, 6, 7]))
    print(solution([30, 10, 23, 6, 100]))
