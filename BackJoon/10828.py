class IntegerStack:

    def __init__(self):
        self._stack = []

    def push(self, value: int):
        self._stack.append(value)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            return -1

    def size(self):
        return len(self._stack)

    def empty(self):
        if not self._stack:
            return 1
        return 0

    def top(self):
        try:
            return self._stack[-1]
        except IndexError:
            return -1


import unittest


class TestIntegerStack(unittest.TestCase):

    def setUp(self) -> None:
        self._command_set = [
            "14",
            "push 1",
            "push 2",
            "top",
            "size",
            "empty",
            "pop",
            "pop",
            "pop",
            "size",
            "empty",
            "pop",
            "push 3",
            "empty",
            "top"
        ]

        for command in self._command_set:
            cmd, value = command.split(" ")

            if cmd in ["push", "pop", "top", "size", "empty"]:
                if cmd == "push":
                    print(s.push(int(value)))
                if cmd == "pop":
                    print(s.pop())
                if cmd == "top":
                    print(s.top())
                if cmd == "size":
                    print(s.size())
                if cmd == "empty":
                    print(s.empty())
            else:
                pass

        self.assertEqual()


if __name__ == '__main__':
    s = IntegerStack()

    command_set = [
        "14",
        "push 1",
        "push 2",
        "top",
        "size",
        "empty",
        "pop",
        "pop",
        "pop",
        "size",
        "empty",
        "pop",
        "push 3",
        "empty",
        "top"
    ]

    for command in command_set:
        cmd, value = command.split(" ")

        if cmd in ["push", "pop", "top", "size", "empty"]:
            if cmd == "push":
                print(s.push(int(value)))
            if cmd == "pop":
                print(s.pop())
            if cmd == "top":
                print(s.top())
            if cmd == "size":
                print(s.size())
            if cmd == "empty":
                print(s.empty())
        else:
            pass
