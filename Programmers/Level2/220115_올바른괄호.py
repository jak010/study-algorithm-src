def solution(s):
    answer = True

    stack = list()
    open_bracket = '('

    for x in s:
        if x == open_bracket:
            stack.append(x)

        else:
            if stack:
                stack.pop()
            else:
                stack.append(x)

    if len(stack) > 0:
        return False
    return True


if __name__ == '__main__':
    s = "()())"
    print(solution(s))
