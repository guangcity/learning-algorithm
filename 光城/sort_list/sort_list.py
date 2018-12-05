class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.quickSort(head,None)
        return head
    def quickSort(self,head,tail):
        if head:
            slow = head
            fast = head.next
            while fast:
                if fast.val<head.val:
                    slow = slow.next
                    tmp = slow.val
                    slow.val = fast.val
                    fast.val = tmp
                fast = fast.next
            tmp = head.val
            head.val = slow.val
            slow.val = tmp
            if head != tail:
                self.quickSort(head,slow)
                self.quickSort(slow.next,None)