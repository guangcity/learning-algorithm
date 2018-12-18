class MinStack {

    private List<Integer> stack = new ArrayList<>();
    private List<Integer> mins = new ArrayList<>();

    /** initialize your data structure here. */
    public MinStack() {
        stack = new ArrayList<>();
        mins = new ArrayList<>();
    }

    public void push(int x) {
        stack.add(x);
        if (mins.size() == 0){
            mins.add(x);
        } else {
            mins.add(Math.min(x, mins.get(mins.size()-1)));
        }
    }

    public void pop() {
        int p = stack.get(stack.size()-1);
        stack.remove(stack.size()-1);
        mins.remove(mins.size()-1);
    }

    public int top() {
        return stack.get(stack.size()-1);
    }

    public int getMin() {
        return mins.get(mins.size()-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */