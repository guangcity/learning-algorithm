**目录**
- <a href="#tm">`题目: 合并两个有序链表`</a>
- <a href="#ckda">`参考答案`</a>
    - <a href="#fa1">`方案1 遍历法`</a>
- <a href="#grzj">`问题`</a>

	
<a id="tm"/>

# 题目：合并两个有序链表 Merge Two Sorted Lists    
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
```
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

<a href="#ckda">

# 参考答案

a href="#fa1">

## 方案1 遍历法
### 【思路】
定义一个结果链表，判断两个链表中的数据大小，将结果存入结果链表中
### 【实现】
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        head = result # 神操作
        
        # 确认 l1 和 l2 为空的场景, 直接返回
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        while True:
            # 比较 l1 和 l2 数据的大小
            if l1.val < l2.val:
                head.val = l1.val
                l1 = l1.next
                if l1 == None:
                    head.next = l2
                    break
                head.next = ListNode(0)
                head = head.next
            else:
                head.val = l2.val
                l2 = l2.next
                if l2 == None:
                    head.next = l1
                    break
                head.next = ListNode(0)
                head = head.next
        return result
```
### 【分析】
时间复杂度：假设一个是$n$个元素，对链表进行遍历($n$)，最终链接所有元素($n+n$)

空间复杂度：因为需要一个数组，所以需要额外的空间。这个空间的大小就是链表元素的个数 $O(n)$

# 遇到的问题
1. ListNode这种资源的操作的方法
```
# 获取 head.val 中的数据，此时的值为 0
head = ListNode(0)
head.val
# 让 head的 next 也成为 ListNode 对象，值也为0
head.next = ListNode(0)
head = head.next  
```
3. head = result 这样的神操作，在不改变原有数据的情况下，操作 result 中的 next 的数据

-----------------------------
欢迎提问，每天晚上都会定期回复~~ 