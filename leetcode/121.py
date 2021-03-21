"""
    121. Best Time to Buy and Sell Stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, minimum = 0, float('inf') 
        
        for price in prices:
            minimum = min(minimum, price) 
            profit = max(profit, price - minimum)
            
        return profit

"""
    - 1116 ms 25.1 MB
    
    # Others
        1. if - 960ms 25.2 MB
            profit, minimum = 0, prices[0]

            for i in range(1, len(prices)):
                if prices[i] - minimum > profit:
                    profit = prices[i] - minimum
                if prices[i] < minimum:
                    minimum = prices[i]
                    
            return profit

    # Tips
        1. Big O of min() and max() is O(n)
        2. min / max > calculating with if
"""