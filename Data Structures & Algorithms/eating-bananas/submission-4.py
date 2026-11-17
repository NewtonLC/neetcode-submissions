class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # In: int[] piles, each pile is a number that represents the bananas in that pile.
        #  - int h, representing the number of hours we have to finish all piles.

        # Out: int k, represents the bananas-per-hour eating rate.
        #  - We're looking to minimize this number.

        # Con:
        # - We must spend minimum 1 hour per pile. We can't eat from more than 1 pile in the same hour.
        # - 1 <= piles.length <= 1,000 --> there can't be 0 piles.
        # - piles.length <= h <= 1,000,000 --> We will have enough time to finish all piles.
        # - 1 <= piles[i] <= 1,000,000,000 --> There won't be empty piles.

        # Ex:
        # piles = [1,4,3,2], h = 9 --> k = 2
        # 2 already works --> no need to look at any other numbers, return 2.

        # Ex:
        # piles = [25,10,23,4], h = 4
        # k needs to be enough to finish all 4 piles, 1 hour each, but not greater than necessary.
        # k = 25 --> 4 hours
        # k = 24 --> 2 hours on pile 0, 3 hours --> 5 hours
        # 25 = max(piles)

        # Edge:
        # - Empty piles? --> no need to consider
        # - No piles? --> No need to consider
        # - Can't finish --> no need

        # Algorithm 1: Brute Force
        # Start with k = 1.
        # Loop: Check if k works --> Iterate through the piles with our rate of k, and then compare our hours to h. --> O(n)
        # If k works, return it.
        # If k does not work, increment it and try again.
        # Time: O(n*m), n = the number of piles, m = max(piles)

        # Algorithm 2: Binary Search
        # k = [1, ... ,max(piles)] --> minimum k that works, every k bigger will also work. 
        #   - For each value of k that doesn't work, every smaller value won't work.
        # 
        # use variables to track left, right boundaries.
        # Start with k = (1+max(piles)) // 2
        # If k works,
        #  - Track this value of k.
        #  - right = k - 1
        # If k does not work,
        #  - left = k + 1

        # Time: O(n*log(m))
        # Space: O(1)

        left, right = 1, max(piles)
        k = right

        while left <= right:
            mid = (left+right) // 2

            # Check if k works
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile/mid)
            
            # Compare num_hours to h.
            if h >= num_hours:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return k




