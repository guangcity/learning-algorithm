class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1=[]
        self.l2=[]
        self.flag=True

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.flag:
            for i in range(len(self.l2)):
                self.l1.append(self.l2.pop())
            self.flag=True
        self.l1.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.flag:
            for i in range(len(self.l1)):
                self.l2.append(self.l1.pop())
            self.flag=False
        return self.l2.pop()
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.flag:
            return self.l1[0]
        else:
            return self.l2[-1]
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.flag:
            return False if len(self.l1)  else True
        else:
            return False if len(self.l2) else True


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
