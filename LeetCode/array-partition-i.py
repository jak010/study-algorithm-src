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


if __name__ == '__main__':
    nums = [1, 4, 3, 2]

    obj = Solution()
    print(obj.arrayPairSum(nums))
