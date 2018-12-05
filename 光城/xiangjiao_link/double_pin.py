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
        size_A = 0
        size_B = 0
        pA = headA
        pB = headB
        while pA or pB:
            if pA:
                size_A += 1
                pA = pA.next
            elif pB:
                size_B += 1
                pB = pB.next
        if size_A > size_B:
            inter = size_A - size_B
            for i in range(inter):
                headA = headA.next
        elif size_A < size_B:
            inter = size_B - size_A
            for i in range(inter):
                headB = headB.next
        return self.search_Node(headA, headB)

    def search_Node(self, headA, headB):
        while headA:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
        return None


