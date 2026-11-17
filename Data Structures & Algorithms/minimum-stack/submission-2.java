class MinStack {
    private Deque<int[]> minStack;

    public MinStack() {
        minStack = new ArrayDeque<>();
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
