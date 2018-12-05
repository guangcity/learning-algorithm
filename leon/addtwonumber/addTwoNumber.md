### Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
### Answer
```c
struct ListNode
{
    long val;
    ListNode *next;
    ListNode(long x) : val(x), next(NULL) {}
};
class Solution
{
  public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {

        printf("l1->val:%ld,l2->val:%ld", l1->val, l2->val);
        ListNode *head = new ListNode((l1->val + l2->val) % 10);
        long val = (l1->val + l2->val) / 10;
        l1 = l1->next;
        l2 = l2->next;
        ListNode *q = head;

        for (; l1 || l2;)
        {
            if (l1 && l2)
            {
                q->next = new ListNode((l1->val + l2->val + val) % 10);
                val = (l1->val + l2->val + val) / 10;
                q = q->next;
                printf("%d\n", q->val);
                l1 = l1->next;
                l2 = l2->next;
            }
            else if (l1)
            {
                q->next = new ListNode((l1->val + val) % 10);
                val = (l1->val + val) / 10;
                q = q->next;
                printf("%d\n", q->val);

                l1 = l1->next;
            }
            else if (l2)
            {
                q->next = new ListNode((l2->val + val) % 10);
                val = (l2->val + val) / 10;
                q = q->next;
                printf("%d\n", q->val);
                l2 = l2->next;
            }
        }

        if ((l1 == NULL || l2 == NULL) && val == 1)
        {
            q->next = new ListNode(1);
            q = q->next;
        }
        return head;
    }
};

```
I think this problem is about Linked List.
Initially,the question define a struct named ListNode which is about the node of LinkedList.
#### Analysis
First,I must define a head pointer to initialize a LinkedList using the way described by the question.
And I will use another pointer to point to head pointer firstly and then use this pointer moving to next pointer to build a LinkedList.
Second,use the "new" critical value instantiate an object using the first value of both l1 and l2 lists.After that ,employ circle to continuously create new nodes.
#### Bug encountered
1. the newer LinkedList is longer than older ones;
2. the operation of pointer is difficult!;
3. the val of newer node must be careful to caculate;
4. ;