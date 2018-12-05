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
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        p = head = ListNode(0)
        for i in l:
            p.next = ListNode(i)
            p = p.next
        p = head.next
        del head
        return p
