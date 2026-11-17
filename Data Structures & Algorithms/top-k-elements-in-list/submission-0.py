class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        In: 
        - int[] nums
        - int k
        Out: 
        - int[] --> top k most frequent elements.

        Con:
        - Answer is always unique
        - Can return output in any order --> [1,2] == [2,1]
        - nums length is between 1 and 10000
        - 1 <= k <= num distinct elements in nums

        Plan:
        - python has import count from collections --> lib that returns counts for each element --> very quick solve
        
        1: Brute Force, Naive Approach
        - Loop through nums, once for each distinct element
        - Use a variable to count the frequency of each element.
        - Add the element to an array
        Time: O(n * d) Space: O(d)

        2: Dictionary approach
        - Loop through nums once
        - For each element, we add it to the dictionary. Key = element, Value = frequency
        - Sort()? --> O(nlogn)
        - Loop through the dictionary, k times.
        - Take the maximum value, and append that key into our result array.
        Time: O(n) Space: O(d)

        '''

        frequency_table = {}
        output = []

        for num in nums:
            if num not in frequency_table:
                frequency_table[num] = 1
            else:
                frequency_table[num] += 1
        
        for _ in range(k):
            most_freq = 0
            most_elem = 0
            # Find k most frequently appearing element
            for key in frequency_table:
                if frequency_table[key] > most_freq:
                    most_elem = key
                    most_freq = frequency_table[key]
            output.append(most_elem)
            del frequency_table[most_elem]
        
        return output




