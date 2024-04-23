import string


def solution(age):
    alphas = string.ascii_letters[0:10]

    answer = []
    age_to_digits = []

    while age > 0:
        age_to_digits.append(age % 10)
        age //= 10

    while len(age_to_digits) > 0:
        c = alphas[age_to_digits.pop()]
        answer.append(c)

    return ''.join(answer)


if __name__ == '__main__':
    print(solution(23))
