class Solution {
    public boolean checkInclusion(String s1, String s2) {
        /*
        in: two Strings, s1 and s2
        out: true/false, does s2 contain a permutation of s1?

        con:
        - only english lowercase letters

        edge/ex:
        - s1 and s2 only contain 1 character. Do they match?
        - s1 = "abc", s2 = "lecabee" --> s2.contains("cab"), which is a permutation of "abc" --> return true
        - s1 = "abc", s2 = "lecaabee" --> No 3-letter sequence of "abc" anywhere in s2. Return false.

        plan:
        - s1 can be permutated in any way, but s2 needs to remain static.
        - s2 can contain letters that aren't anywhere in s1. --> ignore them.
        - Use a freqMap? to track frequencies of each letter in s1.
        - sliding window? --> maintain length equal to s1.length(), we'd compare the contents from s2 with s1.

        s1 = "abc"

        freqMap = {a:1, b:1, c:1}

        s2 = "lecabee" -->
        "lec" --> {a:1, b:1, c:0}
        "eca" --> {a:0, b:1, c:0} --> does every value == 0?
        "caa" --> {a:-1, b:1, c:0}
        ...
        return false
        
        */

        if (s1.length() > s2.length()){
            return false;
        }

        HashMap<Character, Integer> freqMap = new HashMap<>();

        // Add every character in s1 to the frequency map
        for (int i = 0;i < s1.length();i++){
            freqMap.put(s1.charAt(i), freqMap.getOrDefault(s1.charAt(i), 0) + 1);
        }

        // Initialize the sliding window
        int left = 0;
        int right = s1.length();

        for (int i = 0;i < s1.length();i++){
            if (freqMap.containsKey(s2.charAt(i))){
                freqMap.put(s2.charAt(i), freqMap.get(s2.charAt(i)) - 1);
            }
        }

        boolean allZero = true;
        for (int val : freqMap.values()){
            if (val != 0) {
                allZero = false;
                break;
            }
        }
        // return true if it does have all 0's
        if (allZero){
            return true;
        }

        // Iterate through s2.
        while (right < s2.length()){
            System.out.println("left: "  + left + " right: " + right);
            System.out.println(freqMap);

            // Add the character back from the left side
            if (freqMap.containsKey(s2.charAt(left))){
                freqMap.put(s2.charAt(left), freqMap.get(s2.charAt(left)) + 1);
            }
            // Remove the character from the right side
            if (freqMap.containsKey(s2.charAt(right))){
                freqMap.put(s2.charAt(right), freqMap.get(s2.charAt(right)) - 1);
            }
            // Increment left and right pointers
            left++;
            right++;

            // Check if freqMap has all 0's
            allZero = true;
            for (int val : freqMap.values()){
                if (val != 0) {
                    allZero = false;
                    break;
                }
            }
            // return true if it does have all 0's
            if (allZero){
                return true;
            }
        }

        return false;
    }
}
