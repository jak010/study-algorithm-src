def solution(my_string):

    hmap = {}

    for ch in my_string:
        if ch not in hmap:
            hmap[ch] = 0

    return ''.join(hmap.keys())

if __name__ == '__main__':

    print(solution("people"))