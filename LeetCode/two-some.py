"""
Author
  - Jako

Create at:
  - 21.10.03

"""

# [A, B, C, D, E,]

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        if nums[left] + nums[right] == target:
            return [left, right]

        _index = {i: v for i, v in enumerate(nums)}

        nums.sort()
        result = []
        temp = []

        while left < right:

            if nums[left] + nums[right] < target:
                left += 1
            if nums[left] + nums[right] > target:
                right -= 1

            if nums[left] + nums[right] == target:

                for i, v in _index.items():
                    if v == nums[left]:
                        result.append(i)
                    if v == nums[right]:
                        result.append(i)
                    else:
                        temp.append(i)

                for dix in list(temp):
                    _index.pop(dix)

                del temp
                return sorted(set(result))


if __name__ == '__main__':
    # [0,1]
    # nums = [2, 7, 11, 15]
    # target = 9

    # [0,1]
    # nums = [3, 3]
    # target = 6

    # 1,2 Check
    # nums = [3, 2, 4]
    # target = 6

    # 2,4
    # nums = [-1, -2, -3, -4, -5]
    # target = -8

    # 0,2
    # nums = [-10, 7, 19, 15]
    # target = 9

    # [1,2]
    nums = [2, 5, 5, 11]
    target = 10

    obj = Solution()
    print(obj.twoSum(nums, target))
