# 两数相加

今天是小安开始Leetcode刷题的第二题，正文开始ing😎

## 题目描述
给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。[题目原址](https://leetcode-cn.com/problems/add-two-numbers/)
**示例**
> 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
> 输出：7 -> 0 -> 8
> 原因：342 + 465 = 807

## 方法：初等数学

### 思想
我们使用变量来跟踪进位，并从包含最低有效位的表头开始模拟逐位相加的过程。
![两数相加的可视化：342+258=708](https://img-blog.csdnimg.cn/20181207210901837.png)
如两数相加的可视化图所示，我们首先从最低有效位也就是列表 l1 和 l2 的表头开始相加。由于每位数字都应当处于 0...9 的范围内，我们计算两个数字的和时可能会出现“溢出”。例如，$5 + 7 = 12$ 。在这种情况下，我们会将当前位的数值设置为 sum%10，并将进位 $count =sum/10$ 带入下一次迭代。
**请特别注意以下情况：**

|测试用例  |说明  |
|--|--|
| l1=[0,1],l2=[0,1,2] |当一个列表比另一个列表长时。  |
|   l1=[],l2=[0,1]|  当一个列表为空时，即出现空列表。|
|l1=[9,9],l2=[1]|求和运算最后可能出现额外的进位，这一点很容易被遗忘 |
### 代码实现
【C实现】

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head=(struct ListNode *)malloc(sizeof(struct ListNode));//head用于返回新链表
    struct ListNode *tail=head;
    int sum,count=0; //sum用来存储当前位相加，若有进位则count=sum/10
    while(l1!= NULL ||l2!=NULL){
        int x = (l1!=NULL)?l1->val:0;
        int y = (l2!=NULL)?l2->val:0;
        int sum =count+x+y;
        count=sum/10;
        tail->next=(struct ListNode *)malloc(sizeof(struct ListNode));
        tail =tail->next;
        tail->val=sum%10;//相加后存储值为除去进位10
        if(l1!=NULL) l1=l1->next;
        if(l2!=NULL) l2=l2->next;
    }
    if(count>0){//判断最后一位是否需要进位
        tail->next=(struct ListNode *)malloc(sizeof(struct ListNode));
        tail=tail->next;
        tail->val=count;
    }
    tail->next=NULL;
    tail=head;
    head=head->next;
    free(tail);
    return head;//返回头结点的下一节点
    }
```
【Java实现】

```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode tail = head;
        int count = 0;
    while (l1 != null || l2 != null) {
        int x = (l1 != null) ? l1.val : 0;
        int y = (l2 != null) ? l2.val : 0;
        int sum = count + x + y;
        count = sum / 10;
        tail.next = new ListNode(sum % 10);
        tail = tail.next;
        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }
    if (count > 0) {
        tail.next = new ListNode(count);
    }
    return head.next;
        
    }
}
```
【python实现】

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tail = head
        count=0
        while(l1 or l2):
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=count+x+y
            count=s//10
            tail.next=ListNode(s%10)
            tail=tail.next
            if(l1!=None): l1=l1.next
            if(l2!=None): l2=l2.next
        if(count>0):
            tail.next=ListNode(1)
        return head.next
    
```
### 复杂度分析
 - 时间复杂度：$O(max(m,n))$，假设 m 和 n分别表示 l1和 l2的长度，上面的算法最多重复 max(m, n)次。
 - 空间复杂度： $O(max(m,n))$， 新列表的长度最多为max(m,n)+1。
 

# Thanks
一起加油哦~~
