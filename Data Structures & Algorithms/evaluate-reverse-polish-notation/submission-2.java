class Solution {
    public int evalRPN(String[] tokens) {
        /*
        in: String[], integers and operations in string format
        out: int result, we need to calculate the math operation
        
        con:
        - Reverse Polish Notation --> number, followed by number,operator sequences where that operator acts on the current result
        - Division between integers truncates toward zero.
        - Divide by 0? No, it will be valid.

        edge/ex:
        - array of length 1 --> return (int)tokens[0]
        
        Plan:
        - Stack, load in integers to the stack.
        - Read integers, add them to stack
        - When you read an operator, pop two numbers, do the operation.

        */
        Deque<Integer> stack = new ArrayDeque<>();

        int pointer = 0;

        while (pointer < tokens.length){
            try {
                stack.push(Integer.parseInt(tokens[pointer]));
                pointer++;
            } catch (NumberFormatException e) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                String op = tokens[pointer];

                switch (op){
                    case "+":
                        stack.push(num1 + num2);
                        break;
                    case "-":
                        stack.push(num2 - num1);
                        break;
                    case "*":
                        stack.push(num1 * num2);
                        break;
                    case "/":
                        stack.push(num2 / num1);
                        break;
                    default:
                }

                pointer++;
            }
        }

        return stack.pop();
    }
}
