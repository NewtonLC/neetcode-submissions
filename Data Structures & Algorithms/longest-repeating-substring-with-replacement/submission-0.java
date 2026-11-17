class Solution {
    public int characterReplacement(String s, int k) {
        /*
        in: String
        out: int, longest substring with only one distinct character, given up to k substitutions.

        con:
        - only uppercase English characters A-Z
        
        edge/ex:
        - s.length == 1 --> return 1
        - s.length == 2 --> if k > 0? return 2 OR is s[0] == s[1]? return 2. ELSE return 1
        - s = 'XYYX', k = 2 --> return 4
        - s = 'AAABABB', k = 1 --> return 5
        
        match:
        How would we figure out if one substring meets the requirement of having only one distinct character?
        given k substitutions.

        plan:
        Sliding Window
        AAABABB --> A --> AA --> AAA --> AAAB --> AAABA --> BAB --> BABB 

        while the current substring meets the requirement, expand.
        if it no longer meets the requirement, shrink from the left.
        Return the longest found substring length

        How do we store the sliding window contents?
        - A frequency dict, tracks the letters as keys and the amount as the value.
        - Ignoring the most common element(pick one if a tie) do the rest sum up to k or less than k?
        - The max length where ignoring the most common, the rest sum to k.

        The window is valid if...
        window size - count of most frequent char <= k

        If the window is no longer valid, we shrink from the left.
        */

        HashMap<Character, Integer> freq_map = new HashMap<>();
        int result = 0;

        // Sliding window approach
        int left = 0;
        int right = 0;
        int maxFreq = 0;
        while (right < s.length()){
            // Expand the window - add current right character to map
            freq_map.put(s.charAt(right), freq_map.getOrDefault(s.charAt(right), 0) + 1);
            maxFreq = Math.max(maxFreq, freq_map.get(s.charAt(right)));

            // Check if the sliding window is valid, and if not, then shrink from the left until it's valid
            while ((right - left + 1) - maxFreq > k){
                System.out.println(freq_map);
                freq_map.put(s.charAt(left), freq_map.get(s.charAt(left)) - 1);
                left++;
            }
            
            // Increment the result (max valid substring)
            result = Math.max(result, right - left + 1);
            right++;
        }

        return result;
    }
}
