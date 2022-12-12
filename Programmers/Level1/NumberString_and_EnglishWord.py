number_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

import timeit

start = timeit.timeit()


def solution(s):
    answer = s

    if len(answer) > 50:
        return False

    try:
        return int(answer)
    except ValueError:
        pass

    for key in number_dict.keys():
        if key in answer:
            answer = answer.replace(key, number_dict[key])

    return int(answer)


stop = timeit.timeit() - start
print(stop)
