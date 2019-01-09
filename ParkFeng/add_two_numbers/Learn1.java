class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        long num1 = 0;
        long num2 = 0;
        int i1 = 0;
        int i2 = 0;
        while (temp1 != null) {
            num1 += temp1.val * Math.pow(10, i1);
            temp1 = temp1.next;
            i1++;
        }
        while (temp2 != null) {
            num2 += temp2.val * Math.pow(10, i2);
            temp2 = temp2.next;
            i2++;
        }
        long res = num1 + num2;
        ListNode resListNode = new ListNode((int) (res%10));
        ListNode tempNode = resListNode;
        while (res >= 10) {
            res /= 10;
            tempNode.next = new ListNode((int) (res % 10));
            tempNode = tempNode.next;
        }

        return resListNode;
    }
}