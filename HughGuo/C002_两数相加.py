def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        if l1==None:
            return l2
        if l2==None:
            return l1
        q=ListNode(-1)
        p=q
        flag=0
        p1=l1
        p2=l2
        while p1 or p2 or flag:
            sum=flag
            if p1:
                sum=sum+p1.val
                p1=p1.next
            if p2:
                sum=sum+p2.val
                p2=p2.next
            p.next=ListNode(sum%10)
            p=p.next
            flag=sum/10
        return q.next
