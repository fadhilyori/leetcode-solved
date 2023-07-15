class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''.join(e for e in s if e.isalnum()).lower()
        
        return p == p[::-1]