class MinStack {
    /*
    in: a series of commands for a stack
    out: a stack, succesful runs on all commands

    con:
    - Each function should run in O(1) time.
    - This is a Min Stack --> we should have a way to sort it by minimum / retrieve the min at O(1)
    - We also want to retrieve top() at O(1) time
    - --> We'd use two Stacks?

    plan:
    constructor
        Stack (current element, minimum element) --> Stack of tuples
        int min
    
    push --> Use standard Stack push, update the minimum element

    pop --> Use Stack pop, update the minimum element

    top --> Return a copy of the top of the stack, first index

    getMin --> Return a copy of the top of the stack, second index

    */

    private Stack<int[]> minStack;

    public MinStack() {
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        int min = minStack.isEmpty() ? val : Math.min(val, getMin());
        minStack.push(new int[]{val, min});
    }
    
    public void pop() {
        minStack.pop();
    }
    
    public int top() {
        return minStack.peek()[0];
    }
    
    public int getMin() {
        return minStack.peek()[1];
    }
}
