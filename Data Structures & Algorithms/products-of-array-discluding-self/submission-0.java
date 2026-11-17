class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*  in: int[]
            out: int[], output[i] == product of every other element in nums
            
            con:
            - Each product fits in a 32-bit integer --> -2.147B - 2.147B
               - No need to worry about integer overflow
            - each nums[i] is between -30 and 30 (inclusive)
            - nums has anywhere from 2 to 100000 numbers.
            - Follow-up: Solve in O(n) with no division operation
            
            edge:
            - nums.length == 2?
                output[i] == nums[]
            - [1,2,4,6] --> [48,24,12,8]
            - [-1,0,1,2,3] --> [0,-6,0,0,0]

            plan:
            Brute Force:
            - Nested loop
            - For each integer, loop through and calculate the product of the rest of the array.
            - Time: O(n^2), Space: O(n)
            for (int i = 0;i < nums.length;i++){
                for (int j = 0;j < nums.length;j++){

                }
            }

            Start with product:
            - Iterate through the loop, get the full product of nums
            - Iterate through again, but divide each nums[i] into the full product to get output[i]
            - Time: O(n), Space: O(n)

            - How does it handle 0's?
            - There is a zero --> when we get prod, we ignore the 0.
                - the index that the 0 is in (i), output[i] == prod
                - output[j] == 0 for all j != i.
            - There is 2+ zeroes --> return all 0's
        */
        int prod = 1;
        int[] output = new int[nums.length];
        int index_zero = -1;

        // Loop 1: Calculate product
        for (int i = 0;i < nums.length;i++){
            if (nums[i] == 0){
                if (index_zero != -1){
                    return output;
                }
                index_zero = i;
                continue;
            }
            prod *= nums[i];
        }

        // Check if we found 1 zero.
        if (index_zero != -1){
            output[index_zero] = prod;
            return output;
        }

        // Loop 2 (no zero): Find output[i]
        for (int i = 0;i < nums.length;i++){
            output[i] = prod / nums[i];
        }

        return output;
    }
}  
