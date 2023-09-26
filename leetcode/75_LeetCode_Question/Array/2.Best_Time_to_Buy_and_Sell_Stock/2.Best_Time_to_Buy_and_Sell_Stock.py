#!/bin/python3
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

'''given an array of prices of a stock, the indices of each prices are months
Calculate the maximum profit when buy and sell the stock at different months'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = 100000
        for price in prices:
            if price < min_prices: min_prices = price
            elif (price - min_prices) > max_profit:
                max_profit = price- min_prices
        return max_profit

if __name__ == "__main__":
    test4 = Solution()
    print(test4.maxProfit([7,6,4,3,1]))