from typing import List
import sys


class Solution:

    # def maxProfit(self, prices: List[int]) -> int:
    #
    #     max_prices = 0
    #
    #     for i, price in enumerate(prices):
    #         for j in range(i, len(prices)):
    #             max_prices = max(prices[j] - price, max_prices)
    #
    #     print(max_prices)

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # 최대값은 0
        min_price = sys.maxsize

        for price in prices:

            min_price = min(min_price, price)  # 최소값을 계속 갱신
            profit = max(profit, price - min_price)

        return profit


if __name__ == '__main__':
    numbers = [7, 1, 5, 3, 6, 4]

    obj = Solution()
    print(obj.maxProfit(numbers))
