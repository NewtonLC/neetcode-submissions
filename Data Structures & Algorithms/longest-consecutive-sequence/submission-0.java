class Solution {
    public int longestConsecutive(int[] nums) {
        /*
        in: int[]
        out: int, length of longest consecutive sequence

        con:
        - Elements do not need to be consecutive or in order
        - As long as they contain the consecutive sequence, it is fine.
        - Algorithm must be O(n) --> no O(1) space sorting algorithms 

        ex:


        plan:
        - convert to a hash set --> removes duplicates
        - focus on the sequence starts. Once we have the hash set, only grab numbers where number-1 doesn't exist
        - For each sequence start, count how long it goes. (Using the hash set lookup is O(1), so this loop is just O(n))
        */

        //Convert the nums array to a hash set for faster lookup
        HashSet set = new HashSet<>();
        for (int num : nums){
            set.add(num);
        }

        //Iterate through nums.
        // Focus on sequence starts - If for num, num-1 doesn't exist, then we start counting.
        // If num-1 does exist, ignore it.
        int longest_sequence = 0;
        for(int num : nums){
            if (set.contains(num-1)) continue;

            int curr_number = num;
            int curr_sequence = 0;
            while (set.contains(curr_number)){
                curr_number += 1;
                curr_sequence += 1;
            }
            longest_sequence = Math.max(longest_sequence,curr_sequence);
        }
        
        return longest_sequence;
    }
}
