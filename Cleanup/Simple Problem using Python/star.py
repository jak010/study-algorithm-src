"""
It is print *
"""
for i in range(0, 5):
    for j in range(i):
        print("*", end="")
    print()

print("============================")

for a in range(0, 6):
    for b in range(5 - a):
        print("*", end="")
    print()

print("============================")
for q in range(0, 6):
    for p in range(6 - q):
        print(" ", end="")
    for r in range(q):
        print("*", end="")
    print()
