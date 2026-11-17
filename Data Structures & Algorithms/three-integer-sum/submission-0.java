class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /*
        in: int[]
        out: int[][], all triplets [nums[i], nums[j], nums[k]] where the sum == 0, and the indices are distinct

        con:
        - No duplicate triplets
        - Can return the output in any order
        
        edge:
        - nums.length == 3 --> Do the 3 digits add up to 0?

        hint: Recommended time & space
        Time: O(n^2)
        Space: O(1)

        plan: 
        Brute Force:
        - For each element,
            - For each remaining element,
                - For each remaining element, does the sum of it with the other two add to 0?
        - This is a O(n^3) approach

        Sorting is O(n log n). What if we sorted the array before we start checking?
        Sorting first wouldn't bring the time over O(n^2).

        We will ignore duplicate elements that we see.

        */
        
        //First, sort the array
        Arrays.sort(nums);
        List<List<Integer>> output = new ArrayList<>();

        //Next, use the two-sum II approach. Loop through the array to get the first element, then
        //find two other elements using a left and right pointer that add to the negative of that target.
        for (int i = 0;i < nums.length-2;i++){
            // Make sure we don't use the same first digit twice.
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            int left = i+1;
            int right = nums.length-1;

            while (left < right){
                int sum = nums[i] + nums[left] + nums[right];

                if (sum > 0){
                    right -= 1;
                }
                else if (sum < 0){
                    left += 1;
                }
                else {
                    output.add(Arrays.asList(nums[i],nums[left],nums[right]));
                    left += 1;
                    while (nums[left] == nums[left-1] && left < right){
                        left += 1;
                    }
                }
            }
        }
        return output;
    }
}
