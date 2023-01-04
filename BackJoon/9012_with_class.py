class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError as e:
            return -1

    def is_empty(self):
        if len(self._stack) == 0:
            return True
        return False

    def __str__(self):
        for x in self._stack:
            print(x, end='')
        return ''


def find_vps(strings):
    s = Stack()
    answer = ""
    for ch in strings:
        if ch == '(':
            s.push(ch)
        if ch == ')':
            is_empty = s.is_empty()

            if is_empty:
                s.push(ch)
                break
            else:
                s.pop()

    if not s.is_empty():
        answer = "NO"
    else:
        answer = "YES"

    return answer


if __name__ == '__main__':
    number = input()

    for x in range(int(number)):
        input_str = input()
        print(find_vps(input_str))

    # input_str = "(())())"
    # input_str2 = "(()())((()))"
    # print(find_vps(input_str2))
