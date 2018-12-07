## 2.AddTwoNumbers两数相加(链表)

### 题目描述

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807



单链表的定义是这样的：

```python
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
```

###思路

这里给出了三种解法

解法一：只需要按逆序的顺序将各位数加起来即可，有进位的地方标志一下。

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        pNode = ListNode(0)
        pHead = pNode
        val = 0
        while l1 or l2 or val:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            pNode.next = ListNode(val % 10)
            val /= 10
            pNode = pNode.next
        return pHead.next
```

思路一样，但换了种写法：

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        carry = 0
        while node1 or node2:
            ptr.next = ListNode((node1.val if node1 else 0) + (node2.val if node2 else 0) + carry)
            ptr = ptr.next
            carry = ptr.val //10
            ptr.val %= 10
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        if carry:
            ptr.next = ListNode(carry)
        return dummyRoot.next
```

解法二：先把两个数字用int型表示出来，相加之和再存成链表形式：

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sl1 = ''
	    sl2 = ''
	    
	    while l1:
	        sl1 += str(l1.val)
	        l1 = l1.next
	        
	    while l2:
	        sl2 += str(l2.val)
	        l2 = l2.next
	    
	    sum = str(int(sl1[::-1]) + int(sl2[::-1]))
	    
	    head = tail = ListNode(0)
	    
	    for cha in sum[::-1]:
	        cur = ListNode(cha)
	        tail.next = cur
	        tail = cur
	        
	    return head.next
```

上述解法的时间复杂度都是O(max(m,n))，空间复杂度也是O(max(m,n))，其中m和n分别代表两个链表的长度。