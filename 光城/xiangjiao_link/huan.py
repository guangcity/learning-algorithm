# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pA=headA
        while pA.next:
            pA=pA.next
        pA.next=headA
        return self.detectCycle(headB)
    def detectCycle(self, head):
        if not head:
            return None
        slow = fast = head
        while(slow and fast): 
            slow, fast =slow.next, fast.next
            if fast:
                fast = fast.next
                if slow is fast:  
                    while(slow is not head):
                        slow, head = slow.next, head.next
                    return head
        return None