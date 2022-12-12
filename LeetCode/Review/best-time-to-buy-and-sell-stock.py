from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        save_pay = 0

        if not prices or len(prices) == 1:
            return save_pay

        # 최소값은 첫번째로 설정
        _current_min_number = prices[0]

        for value in prices:

            if value < _current_min_number:
                _current_min_number = value
            # 저점 타이밍

            # save_pay = min(_current_min_number - value, save_pay)
            if _current_min_number - value < save_pay:
                save_pay = _current_min_number - value

        return abs(save_pay)


if __name__ == '__main__':
    # nums = [7, 1, 5, 3, 6, 4]

    # nums = [7, 6, 4, 3, 1]

    # nums = [2, 4, 1]

    nums = [2, 1, 2, 1, 0, 1, 2]

    obj = Solution()
    print(obj.maxProfit(nums))
