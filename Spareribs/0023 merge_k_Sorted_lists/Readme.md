**目录**
- <a href="#tm">`题目: 合并K个排序链表`</a>
- <a href="#ckda">`参考答案`</a>
    - <a href="#fa1">`方案1 遍历法`</a>
- <a href="#grzj">`问题`</a>

<a id="tm"/>

# 题目: 合并K个排序链表

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
```
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
```
<a id="ckda"/>

# 参考答案

<a id="fa1"/>

## 方案1 遍历法
### 【思路】
遍历 lists 中所有ListNode()数据，排序后创建链表。
### 【实现】
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 将所有的数存入一个空列表中
        _nums = []
        for _listnode in lists:
            while  _listnode:
                _nums.append(_listnode.val)
                _listnode = _listnode.next
        
        # 如果列表为空, 直接返回
        if _nums == []:
            return []
        
        # 对数据进行排序
        _nums.sort()
        print(_nums)
        
        # 将结果整理到ListNode中
        res = ListNode(0)
        answer = res
        for _num in _nums:
            res.next = ListNode(0)
            res = res.next
            res.val =_num
            
        # 需要去掉链表中第一个值
        return answer.next
```
### 【分析】
时间复杂度：假设一个是$n$个元素，对链表进行遍历($n$),对数组进行排序(排序算法可以达到$nlogn$)，最终链接所有元素($n$),就是 （ $n+nlogn+n$），也就是  $O(nlogn)$

空间复杂度：因为需要一个数组，所以需要额外的空间。这个空间的大小就是链表元素的个数 $O(n)$

<a id="wt"/>

# 问题
1. 需要总结一份ListNode(0) 这种结构的使用方式


博客地址：[LeetCode刷题日记](https://blog.csdn.net/q370835062/column/info/30688) 欢迎关注，留言~~~
