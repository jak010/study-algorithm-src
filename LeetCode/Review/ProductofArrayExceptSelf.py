from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        # 왼쪽 곱셉의 결과를 구함 (마지막 원소는 제외)
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]  # 배열의 원소를 곱

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #
    #     left = 0
    #     right = len(nums)
    #
    #     _temp = list(nums)
    #
    #     for _id, value in enumerate(nums):
    #         _index = [x for x in range(left, right)]
    #         _index.pop(_id)
    #
    #         init = 1
    #         for x in _index:
    #             init *= _temp[x]
    #
    #         nums[_id] = init
    #
    #     return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]

    obj = Solution()
    print(obj.productExceptSelf(nums))
