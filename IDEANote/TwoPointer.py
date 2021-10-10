strings = ['a', 'b', 'c', 'd', 'e']

# Two Pointer?
## 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
## Basic

sp, ep = 0, len(strings) - 1

print(strings)
while sp < ep:
    # ep를 sp에다가 넣으면 뒤에것이 첫 번쨰 인덱스로 이동함
    # sp를 ep에다가 넣으면 앞에것이 마지막 인덱스로 이동함

    strings[sp], strings[ep] = strings[ep], strings[sp]
    # print(strings)
    sp += 1
    ep -= 1

########################################################################
# 내림차순으로 정렬된 정수 배열이 주어지면 내림차순으로 정렬된 각 숫자의 제곱 배열 #
#######################################################################
number = [16, 8, 4, 2, 1]
# result = [25,16,9,4,1]

sp = 0
ep = len(number) - 1
mp = int(len(number) / 2)
idx = 0

while sp < ep:
    number[sp], number[ep] = number[sp] ** 2, number[ep] ** 2

    sp += 1
    ep -= 1
else:
    number[mp] = number[mp] ** 2

print(number)