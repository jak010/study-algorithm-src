count = int(input())

for x in range(count, 0, -1):

    for y in range(1, x):
        print(" ", end="")
    print("*" * (count + 1 - x))

"""output
    *
   **
  ***
 ****
*****
"""


# count = 5

# for x in range(count + 1, 0, -1):
#
#     for y in range(1, x):
#         print("*", end="")
#     print("")
