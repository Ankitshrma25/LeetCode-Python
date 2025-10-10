from typing import List
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = math.inf
        ## Itrating through each prince for the least number
        for price in prices:
            min_price=min(min_price, price)
            # Today's profit
            current_profit = price - min_price
            # max profit
            max_profit = max(max_profit, current_profit)
        return max_profit
    
solution = Solution()
print(f"Maximum Profit is: {solution.maxProfit([7,3,1,6,3,10])}")