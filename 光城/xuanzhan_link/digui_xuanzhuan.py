# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None or head.next is None:
            return head
        for i in range(k):
            head = self.rightShift(head)
        return head

    def rightShift(self, head):
        pre = head
        curr = head.next
        while curr:
            if curr.next is None:
                curr.next = head
                pre.next = None
                return curr
            pre = pre.next
            curr = curr.next
        return curr
