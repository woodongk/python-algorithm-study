from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = max(prices)

        # 포문을 걸어서 최고점에 사고 최고가에 팔기
        # two pointer solution
        profit = 0
        buy_idx = sell_idx = 0
        while True:

            # 1. 구매시점 구하기
            print("buy idx = {}".format(buy_idx))
            try:
                while prices[buy_idx] > prices[buy_idx + 1]:
                    buy_idx += 1
                print("new buy idx = {}".format(buy_idx))
            except IndexError:
                break

            sell_idx = buy_idx + 1

            # 2. 매매시점 구하기
            print("sell idx = {}".format(sell_idx))
            try:
                while prices[sell_idx] <= prices[sell_idx + 1]:
                    sell_idx += 1
                print("new sell idx = {}".format(sell_idx))
            except IndexError:
                sell_idx = len(prices) - 1

            # 갱신
            profit += prices[sell_idx] - prices[buy_idx]
            buy_idx = sell_idx
            print("profit is now {}".format(profit))
            print()
        return profit

if __name__ == '__main__':
    sol = Solution()
    #sol.maxProfit([7,1,5,3,6,4])
    sol.maxProfit([1,2,3,4,5])