class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
        return p1