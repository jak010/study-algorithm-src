# number = int(input())


# for x in range(1, number + 1):
#
#     for number in ['3', '6', '9']:
#         if number in str(x):
#             print("X", end=' ')
#             break
#
#     else:
#         print(x, end=" ")

# Enhanced Solution

number = int(input())
for x in range(1, number + 1):
    if str(x % 10) in ['3', '6', '9']:
        print("X", end=" ")
    else:
        print(x, end=" ")
