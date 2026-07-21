/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0 || lists == null) {
            return null;
        }

        while (lists.length > 1) {
            List<ListNode> temp = new ArrayList<>();
            ListNode l1, l2;
            for (int i=0; i<lists.length; i+=2) {
                l1 = lists[i];
                l2 = i+1<lists.length ? lists[i+1] : null;
                temp.add(mergeLists(l1,l2));
            }
            lists = temp.toArray(new ListNode[temp.size()]);
        }
        return lists[0];
    }

    public ListNode mergeLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }

        if (l1 != null) {
            curr.next = l1;
        } else {
            curr.next = l2;
        }
        return dummy.next;
    }
}
