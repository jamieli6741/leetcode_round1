# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next=head)
        curr = dummy_head
        while curr.next and curr.next.next:
            tmp1 = curr.next
            tmp3 = curr.next.next.next
            curr.next = curr.next.next
            curr.next.next = tmp1
            tmp1.next = tmp3
            curr = curr.next.next

        return dummy_head.next
