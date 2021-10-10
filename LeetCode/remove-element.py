from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums: return len(nums)

        if val in nums:
            for index in range(len(nums)):
                for idx, value in enumerate(nums):
                    if value == val:
                        nums.append('_')
                        nums.pop(idx)
            if nums.index('_'):
                return len(nums[:nums.index('_')])
            else:
                return 0
        else:
            return len(nums)


if __name__ == '__main__':
    # nums = []
    # val = 0

    # nums = [3, 2, 2, 3]
    # val = 3

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 5

    obj = Solution()
    print(obj.removeElement(nums, val))
