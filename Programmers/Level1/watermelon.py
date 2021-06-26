
n = 3

strings = ""
for x in range(1,n+1):
    if x % 2 != 0:
        strings += "수"
    else:
        strings += "박"

print(strings)
