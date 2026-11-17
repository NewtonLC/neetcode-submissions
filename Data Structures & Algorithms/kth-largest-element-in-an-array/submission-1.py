import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # In: 
        # int[] nums, unsorted
        # int k, --> kth largest element

        # Out:
        # int, kth largest element
        # Elements are not guaranteed to be distinct.
        # If we have 5, 5, 4, and we want to return the third largest element, we return 4.

        # Con:
        # - 1 <= k <= nums.length <= 10000 --> k cannot be out of bounds.
        # 

        # Algorithm 1: Sorting
        # Use Python's built-in sorting method, sort(nums)
        # Return nums[k].
        # Time: O(n log n)
        # Space: O(1)

        # Algorithm 2: Min-Heap
        # Min-Heap is a BT that keeps the smallest value at the top.
        # nums = [2,3,1,1,5,5,4], k = 3
        # Create a minHeap that tracks the top k values
        # Loop through nums and add push-pop when we see any values larger than the top of the minHeap
        # At the end of nums, our minHeap should contain the top k elements of the nums array
        # And we can simply return the top.
        # Time: O(n log k)
        # Space: O(k)

        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for num in nums[k:]:
            if num > minHeap[0]:
                heapq.heappushpop(minHeap, num)
        
        return minHeap[0]





