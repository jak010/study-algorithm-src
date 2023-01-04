# #Stack

count = 6
x = "(())())"
x1 = "(((()())()"
x2 = "(()())((()))"
x3 = "((()()(()))(((())))()"
x4 = "()()()()(()()())()"
x5 = "(()((())()("


def find_stack(strings):
    stack = []
    for x in strings:
        if x == '(':
            stack.append(x)
        if x == ')':
            if len(stack) == 0:
                stack.append(x)
                break
            else:
                stack.pop()

    if len(stack) != 0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    # count = int(input())

    print(find_stack(x))
