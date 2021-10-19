from typing import List
from itertools import permutations


class Solution:

    # My Solution is ...
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        for k, v in enumerate(nums):

            if k % 2 != 0:
                result += min(nums[k - 1:k + 1])
        return result

    # Solve 01
    # def arrayPairSum(self, nums: List[int]) -> int:
    #     sum = 0
    #     nums.sort()
    #
    #     for i, n in enumerate(nums):
    #         if i % 2 == 0:
    #             sum += n
    #     return sum

    # def arrayPairSum(self, nums: List[int]) -> int:
    #     return sum(sorted(nums)[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]

    obj = Solution()
    print(obj.arrayPairSum(nums))
