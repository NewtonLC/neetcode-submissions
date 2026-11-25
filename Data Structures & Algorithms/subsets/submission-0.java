class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        /*
        in: int[], all unique integers
        out: int[][], all possible subsets

        con:
        - all unique ints
        - For each subset, ask: Does it contain num? for all num in nums.
        --> 2^n time and space

        edge/ex:
        - {1,2,3} --> 000 001 010 011 100 101 011 111

        Recursion:
        - Base case: Return the given array (empty array at start)
        - Recursive case: Return the given array concat with num in nums.
        
        Dynamic programming:
        - Have a set of int sets. Add to the set, then add to the set again based on what's already in the set
        - Time: O(2^n) Space: O(2^n) outside of result 

        */

        List<List<Integer>> dp = new ArrayList<>();
        List<Integer> empty = new ArrayList<>();
        dp.add(empty);

        for (int num : nums){
            List<List<Integer>> dpTemp = new ArrayList<>();
            for (List<Integer> subset : dp){
                if (subset.size() == 0){
                    List<Integer> newSubset = new ArrayList<>();
                    newSubset.add(num);
                    dpTemp.add(newSubset);
                }
                else {
                    List<Integer> newSubset = new ArrayList<>(subset);
                    newSubset.add(num);
                    dpTemp.add(newSubset);
                }
            }
            dp.addAll(dpTemp);
        }

        return dp;
    }
}
