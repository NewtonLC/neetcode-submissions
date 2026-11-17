class Solution:
    def isValid(self, s: str) -> bool:
        '''
        in: s --> [], (), {}
        out: true/false

        con:
        - Every open bracket is closed by the same type --> (), [], {}
        - Brackets are closed in the correct order --> {()}, not {(})
        - Every closed bracket has a corresponding open bracket of the same type --> (), no [])
        - no ''

        Two pointer approach:


        plan: Use a stack
        Stacks are LIFO --> Last in first out
        
        Loop through the characters in the input string.

        If we see an open bracket, add it to the stack.

        If we see a closed bracket... check the top of the stack
            If the item at the top does not match, return false.
            If the item does match, pop from the stack
        
        After finishing the loop, if our stack is empty, return True. Otherwise, return False.

        {([])}[]

        Stack: []
        '''

        stack = []

        for c in s:
            print(c)
            print(stack)
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (top == '[' and c == ']') or (top == '(' and c == ')') or (top == '{' and c == '}'):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0