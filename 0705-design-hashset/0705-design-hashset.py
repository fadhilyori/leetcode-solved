class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 10**5
        self.set = [None] * self.size

    def _hash(self, key: int) -> int:
        return hash(key) % self.size

    def add(self, key: int) -> None:
        hashed_idx = self._hash(key)
        if self.set[hashed_idx] is None:
            self.set[hashed_idx] = ListNode(key)
        else:
            cur = self.set[hashed_idx]

            while cur:
                if cur.key == key:
                    return
                if cur.next is None:
                    cur.next = ListNode(key)
                    return
                cur = cur.next
        

    def remove(self, key: int) -> None:
        hashed_idx = self._hash(key)
        
        if self.set[hashed_idx]:
            if self.set[hashed_idx].key == key:
                self.set[hashed_idx] = self.set[hashed_idx].next
                return
            cur = self.set[hashed_idx]

            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next

    def contains(self, key: int) -> bool:
        hashed_idx = self._hash(key)
        cur = self.set[hashed_idx]

        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)