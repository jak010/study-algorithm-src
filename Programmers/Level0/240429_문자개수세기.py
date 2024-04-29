import string


def solution(my_string):

    ascii_letters = string.ascii_uppercase + string.ascii_lowercase

    return [my_string.count(ch) for ch in ascii_letters]


if __name__ == '__main__':
    print(solution("Programmers"))
