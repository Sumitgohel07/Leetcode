class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cp = None
        for i in prices:
            if cp==None:
                cp = i
            else:
                if i < cp:
                    cp = i
            profit = i - cp
            if profit > max_profit:
                max_profit = profit
        return max_profit