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
