# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = None
        c1 = l1
        c2 = l2
        tail_r = None
        carry = 0
        
        while c1 is not None or c2 is not None or carry != 0:
            v1 = c1.val if c1 is not None else 0
            v2 = c2.val if c2 is not None else 0
                
            s = v1 + v2 + carry
            d = s % 10
            carry = s // 10
            
            newNode = ListNode(d)
            
            if r is None:
                r = newNode
                tail_r = r
            else:
                tail_r.next = newNode
                tail_r = tail_r.next
            
            c1 = c1.next if c1 is not None else None
            c2 = c2.next if c2 is not None else None
            
        return r
            
        
        
        