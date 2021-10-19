from collections import OrderedDict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    output.append(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return (list(set(output)))


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    obj = Solution()
    print(obj.threeSum(nums))
