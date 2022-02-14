import string

alphabet = string.ascii_letters[0:26]
result = [None] * len(alphabet)

s = "baekjoon"

# My Solve
for ch1 in alphabet:
    for ch2 in s:
        if alphabet.find(ch2) != -1:
            result[alphabet.index(ch2)] = s.index(ch2)

for k, v in enumerate(result):
    if v is None:
        result[k] = -1

    print(result[k], end=" ")

# Enhancement
alphabet = string.ascii_letters[0:26]
s = input()
for x in alphabet:
    print(s.find(x), end=" ")
