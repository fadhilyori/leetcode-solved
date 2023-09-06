# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Calculate the size
        head_size = 0
        cur = head
        
        while cur:
            head_size += 1
            cur = cur.next
            
        part_size, remainder = divmod(head_size, k)
        result = []
        cur = head
        
        for i in range(k):
            result.append(cur)
            if remainder > 0:
                cur_part_size = part_size + 1
                remainder -= 1
            else:
                cur_part_size = part_size
                
            for j in range(cur_part_size - 1):
                cur = cur.next
                
            if cur:
                cur.next, cur = None, cur.next
            
        
        return result