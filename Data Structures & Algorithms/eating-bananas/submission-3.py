class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # In: List of ints, int[] where each int represents a pile of bananas
        # - int h, representing the number of hours you have.
        # Out: int k, bananas-per-hour eating rate. How many bananas do you eat per hour?
        # - k needs to be enough for us to finish all piles of bananas by h hours.
        # - We want to MINIMIZE k.

        # Con:
        # - there are 1 to 1000 piles. --> Can't have 0 or negative number
        # - piles.length <= h <= 1000000 --> We can't have more piles than hours. --> We'll always have enough time.
        # - each pile contains 1 to 1 billion bananas. --> We can't have empty piles.

        # Ex:
        # - piles = [1,4,3,2], h = 9
        # --> k = 1
        # piles[0] --> 1 hr
        # piles[1] --> 4 hrs
        # piles[2] --> 3 hrs
        # piles[3] --> 2 hrs
        # piles --> 10 hrs > h. --> k = 1 does not work.
        
        # Ex:
        # piles = [25,10,23,4], h = 4
        # k = 25 --> 4 hrs

        # Plan: Brute Force
        # Start with 1
        # Check if it works. --> O(n)
        # If it doesn't work, increment k by 1.
        # If it does work, return k.
        # --> Time: O(n*m). n = number of piles, m = max(piles)

        # Plan: Binary Search
        # Start with two boundaries, left = 1, right = max(piles)
        # Check if the middle value works ((left+right) // 2) --> O(n)
        # If it doesn't work...
        #  - We know that every smaller value also does not work.
        #  - left = middle
        # If it does work....
        #  - We know that every larger value also works.
        #  - We're unsure if this value is the minimum k.
        #  - right = middle
        #  - Track the current value. k = middle
        
        left, right = 1, max(piles)
        k = right

        while left <= right:
            mid = (left+right) // 2

            # Check if mid works
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile/mid)
            
            if num_hours <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return k
