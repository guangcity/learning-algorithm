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
        if k==0 or head is None or head.next is None:
            return head
        p=head
        size=0
        while p:
            size+=1
            p=p.next
        # 所循环的真实k
        # 真实k为原始k除以链表长度取模
        k=k%size
        p=head
        pre=head
        curr=head.next
        '''
        (1)真实k如果不为0，参照算法图
        (2)真实k如果为0，也就是原始k能够整除链表长度，
        那么此时的节点旋转后还是原链表，直接返回原链表
        '''
        if k:
            for i in range(size-k):
                pre=p
                curr=p.next
                p=p.next
            pre.next=None
            newhead=curr
            while curr.next:
                curr=curr.next
            curr.next=head
            return newhead
        return head