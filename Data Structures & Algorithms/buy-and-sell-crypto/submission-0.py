class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # In: int[] prices, index i is referring to the day.
        # Out: int, max profit you can achieve from prices.
        
        # Con:
        # - We can only choose one day to purchase and one day to sell.
        # - We can choose to make no transactions --> maxProfit >= 0
        # - There will always be 1 to 100 days in prices.
        # - All prices will be nonnegatives 0 to 100.

        # Edge:
        # - What happens when there is one day? --> Return 0.

        # Plan: Sliding Window
        # Brute Force --> Iterate through all possible price differences, return max.
        # --> O(n^2) time, O(1) space.
        # Sliding Window allows us to iterate through prices once
        # --> O(n) time, O(1) space. --> Most efficient

        # Left edge --> Purchase date
        # Right edge --> Selling date

        # [10,1,5,6,7,1]
        # [10] --> [1]
        # [1] --> [1,5]
        # [1,5] --> [1,5,6]
        # [1,5,6] --> [1,5,6,7]
        # [1,5,6,7] --> [1,5,6,7,1]

        # [10,2,5,6,7,1,11]
        # [2,5,6,7] --> [1]

        maxProfit = 0
        left = 0
        right = 0

        while right < len(prices) - 1:
            right += 1

            if prices[right] < prices[left]:
                left = right
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
        
        return maxProfit
