from typing import List


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

    # Solve 02
    def solve02(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    # Solve 03
    # def solve03(self, nums: List[int]) -> int:
    #     result = 0
    #     depth = 2
    #     nums.sort()
    #
    #     for i in range(0, len(nums), depth):
    #         result += min(nums[i:i + depth])
    #
    #     return result


if __name__ == '__main__':
    nums = [1, 4, 3, 2]

    """
    [6,2,6,5,1,2] -> [1,2,2,5,6,6]
    [1,2] [2,5] [6,6] 
    1, 2, 6
    
    """

    obj = Solution()
    print(obj.arrayPairSum(nums))
    print(obj.solve02(nums))
