class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            return self.queue.pop(0)
        return None
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.queue[0]
        return None
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        queue_len=len(self.queue)
        if queue_len==0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
