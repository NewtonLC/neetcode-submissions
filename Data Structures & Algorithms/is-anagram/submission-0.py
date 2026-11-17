class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case: If s and t are different lengths, return False
        if len(s) != len(t):
            return False
        
        # Looking for a solution that is O(1) in space and ideally O(n+m) time
        # A hash table solution is ALREADY O(1) because of the constraint of 26 english characters.

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT