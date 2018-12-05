# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        size = 0
        while p:
            size += 1
            p = p.next
        for i in range(size - 1):
            l = head
            for j in range(size - i - 1):
                p = l
                p1 = l.next
                if (p.val > p1.val):
                    temp = p.val
                    p.val = p1.val
                    p1.val = temp
                l = l.next
        return head
