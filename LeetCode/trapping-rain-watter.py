from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        volume = 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left_max <= right_max:

            left_max = min(left_max, height[left])
            right_max = min(right_max, height[right])

            if left <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


if __name__ == '__main__':
    height = [0, 1, 0,  #
              2, 1, 0,  #
              1, 3, 2,  #
              1, 2, 1]

    obj = Solution()
    obj.trap(height)
