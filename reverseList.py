class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
  
class Solution:
    def reverseList(self, head):
        dummy = ListNode(0)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next

a = ListNode(5)
a = ListNode(7)
c = Solution()
c.reverseList(a)
