from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        height = [height[x:x + 3] for x in range(0, len(height), 3)]

        from pprint import pprint
        pprint(height)


if __name__ == '__main__':
    height = [0, 1, 0,  #
              2, 1, 0,  #
              1, 3, 2,  #
              1, 2, 1]

    obj = Solution()
    obj.trap(height)
