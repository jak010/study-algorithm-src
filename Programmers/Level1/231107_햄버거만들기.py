items = [2, 1, 1, 2, 3, 1, 2, 3, 1]

_stack = []

count = 0
for item in items:
    _stack.append(item)

    if _stack[-4:] == [1, 2, 3, 1]:
        del _stack[-4:]
        count += 1

print(items)
print(_stack)
