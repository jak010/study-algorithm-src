"""
@ data : 2020-11-15
@ author : jak010
@ description : 소수 판단 알고리즘 ?

소수 (PRIME NUMBER)
1 과 자기자신을 약수로 가지는 수
"""
# !/usr/bin/python3

NUMBER = 221
count = 0

divideNumber = []

for x in range(1, NUMBER + 1):
    if prime % x == 0:
        if (x != 1) or (x != prime):
            divideNumber.append(x)
            count += 1

print(divideNumber)

if count > 2:
    print("is not prime")
else:
    print("is prime ")
