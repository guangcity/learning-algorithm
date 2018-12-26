/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(head == NULL)
            return NULL;
        ListNode *right = head;
        while(right->next)
            right = right->next;
        QuickSort(head, right);
        return head;
    }
private:
    void QuickSort(ListNode *left, ListNode *right)
    {
        if(left != right)
        {
            ListNode *partion = GetPartion(left, right);
            QuickSort(left, partion);
            if(partion->next)
                QuickSort(partion->next, right);
        }
    }
    ListNode *GetPartion(ListNode *left, ListNode *right)
    {
        int key = left->val;
        ListNode *p = left;
        ListNode *q = p->next;
        
        while(q != right->next)
        {
            if(q->val < key)
            {
                p = p->next;
                swap(p->val, q->val);
            }
            q = q->next;
        }
        swap(p->val, left->val);
        return p;
    }
};