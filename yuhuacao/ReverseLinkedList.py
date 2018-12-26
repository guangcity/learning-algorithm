题目:
给定一个链表，把这个链表反转过来。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
解题思路：
比较简单，对链表遍历，需保存上一个指针和下一个指针。在遍历过程中理清三者关系，注意不要互相覆盖即可。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return []
        last_temp = None
        temp = head
        while(temp!=None):
            temp_next = temp.next
            temp.next = last_temp
            last_temp = temp
            temp = temp_next
        
        return last_temp
