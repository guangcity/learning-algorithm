class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.stack.pop()
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.stack[-1]
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.stack:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)