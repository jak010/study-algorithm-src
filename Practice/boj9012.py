# boj 9012
# Stack
# 괄호 문자열 문제


test1 = "(())())"
test2 = "()"
test3 = "(())"

stack = []
ans = "YES"
for c in test3:
    if c == '(':
        stack.append(c)
    else:
        if len(stack) > 0:
            stack.pop()
        else:
            ans = "NO"

print(ans)
