class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        stackA=[]
        stackB=[]
        while headA or headB:
            if headA:
                stackA.append(headA)
                headA=headA.next
            elif headB:
                stackB.append(headB)
                headB=headB.next
        if stackA[-1]!=stackB[-1]:
            return None
        while stackA and stackB:
            res=stackA[-1]
            stackA.pop()
            stackB.pop()
            if stackA and stackB:
                if stackA[-1].val!=stackB[-1].val:
                    return res
            else:
                return res
        return None