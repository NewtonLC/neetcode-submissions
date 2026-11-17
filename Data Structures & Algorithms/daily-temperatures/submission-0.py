class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # In: int[], temperatures
        # Out: int[], result
        # - temperatures and result have the same length
        # - Last element of result will always be 0, there is no following day.
        # E:
        # - One element --> [0]

        # Notes: We want to use a MONOTIC DECREASING STACK.
        # - This is a stack whose values are only decreasing or staying the same.
        # - As we add values to the stack, we check if they are greater.
        # - If greater, we pop from the stack (smallest values popped first) until no values are greater than the current.
        # - After popping, we append the new value(and index!) onto the stack.

        # - We NEED to track both the temperature AND the index in the stack, in order to calculate the distance between the indices.
        # - My previous approach failed because I was trying to ONLY track the temperatures within the stack, then pop them in order.
        # - ^ This would not have worked. I should have been more flexible in how I use stacks, and considered more approaches that
        #   better utilized the stack.

        # Initialize result and stack
        res = [0] * len(temperatures)
        stack = []

        # Loop through each element in temperatures.
        for i, t in enumerate(temperatures):
            # As long as there are elements in the stack that are SMALLER than the current temperature, pop them.
            # When you pop them, take the distance between their index(stored in stack) and the current index, and store it in res.
            # To access the current temperature, get the last element(stack[-1]), then get the temperature(stack[-1][0]).
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            # After popping, append the new temp and index.
            stack.append([t,i])
        
        return res
        


        