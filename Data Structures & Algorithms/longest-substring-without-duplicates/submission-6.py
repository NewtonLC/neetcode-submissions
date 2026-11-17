class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        In: string s
        Out: int, length of the longest substring (that cannot contain repeating characters)
        Con:
        - substring cannot contain repeating characters
        - 0 <= s.length <= 50,000
        - printable ASCII characters
        Edge:
        - len(s) == 0 --> return 0

        Algorithm: Sliding Window
        zxyzxyz

        check if the string is not empty
        left, right = 0
        max length var = 1
        set() --> avoid duplicates, track chars in sliding window

        repeat until right >= len(s) - 1
            *assume that left and right are initialized*
            check if the next character is a duplicate --> does set() contain the next character
                If yes, JUMP
                    Move left to --> right + 1. Move right to right + 1
                    clear set()
                If no, EXTEND
                    Increase right by 1
                    if max length < right - left + 1, update max length
        
        return max length


        New JUMP algorithm:

        While s[right+1] is in set:
            remove s[left] from set.
            iterate left by 1.

        '''

        if len(s) == 0:
            return 0

        left = 0
        right = 0
        max_length = 1
        sliding_window = set(s[0])

        while right < len(s) - 1:
            if s[right+1] in sliding_window:
                while s[right+1] in sliding_window:
                    sliding_window.remove(s[left])
                    left += 1
                #right = left
                #sliding_window = set(s[left])
            else:
                right += 1
                sliding_window.add(s[right])
                max_length = max(max_length, right - left + 1)
        
        return max_length

