# Input: n = 234


# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        each_list = []

        while n > 0:
            each_list.append(int(n % 10))
            n //= 10

        each_multiplier = 1
        for x in each_list:
            each_multiplier = each_multiplier * x

        each_sum = sum(each_list)

        return each_multiplier - each_sum

    def solution2(self, n: int) -> int:
        prod = 1
        sums = 0

        while n != 0:
            last = n % 10
            prod *= last
            sums += last
            n = n // 10
        return prod - sums


# Other Solution
# def subtractProductAndSum(self, n: int) -> int:
#     prod = 1  # n =234
#     sums = 0
#     while n != 0:  # 1st loop     2nd loop    3rd loop
#         last = n % 10  # last =    4            3           2
#         prod *= last  # prod =    1*4 = 4      4*3 = 12    12*2 = 24
#         sums += last  # sums =    0+4 = 4      4+3 = 7     7+2 = 9
#         n = n // 10  # n    =    23           2           0
#     return prod - sums  # 24 - 9 = 15


if __name__ == '__main__':
    import operator
    from functools import reduce

    n = 4421

    sol = Solution()
    print(sol.subtractProductAndSum(n))

    a = map(int, str(n))
    print(reduce(operator.mul, a) - sum(a))
