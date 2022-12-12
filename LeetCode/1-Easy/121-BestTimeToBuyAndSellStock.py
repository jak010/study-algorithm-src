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

    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0  # 최대값은 0
    #     min_price = sys.maxsize
    #
    #     for price in prices:
    #
    #         min_price = min(min_price, price)  # 최소값을 계속 갱신
    #         profit = max(profit, price - min_price)
    #
    #     return profit

    # 틀린 접근법
    # def maxProfit(self, prices: List[int]) -> int:
    # 
    #     if len(prices) == 1:
    #         return 0
    # 
    #     min_value = min(prices[:-1])
    #     min_index = prices.index(min_value)
    # 
    #     search_result = [x - min_value for x in prices[min_index:]]
    # 
    #     if not search_result:
    #         return 0
    # 
    #     result = max(search_result)
    #     if result < 0:
    #         return 0
    # 
    #     return result

    # 22.04.04, 생각해서 풀어봄
    def maxProfit(self, prices: List[int]) -> int:
        money = 999999
        max_value = 0
        for idx, value in enumerate(prices):
            money = min(money, value)  # 최소값 갱신함

            profit = value - money  # 이익금 = 원소 - 최소값

            max_value = max(max_value, profit)  # 최대값(원소에서 - 최소값)으로 갱신

        return max_value

    # 22.04.04, 생각해서 풀어봄
    def maxProfit2(self, prices: List[int]) -> int:
        money = 999999
        max_value = 0
        for value in prices:
            money = min(money, value)  # 최소값 갱신함
            # profit = value - money  # 이익금 = 원소 - 최소값

            max_value = max(max_value, value - money)  # 최대값(원소에서 - 최소값)으로 갱신

        return max_value


if __name__ == '__main__':
    # 최대 수익을 낼 수 있는 날을 찾는다
    # 저점인 날을 찾는다
    #   - 저점인 이전 날에는 팔 수 없다
    # 고점인 날을 찾는다
    #   - 고점 - 저점 = 수익
    # 가장 많은 수익이 되는 날을 찾는다.

    # prices = [7, 1, 5, 3, 6, 4]  # 5
    # prices = [7, 6, 4, 3, 1]  # 0
    # prices = [2, 4, 1] # 2
    # prices = [1, 2] # 1
    # prices = [3, 2, 6, 5, 0, 3]  # 4

    obj = Solution()
    print(obj.maxProfit(prices))
