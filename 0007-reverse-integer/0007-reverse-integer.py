class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        is_below_zero = x < 0
        x = abs(x)
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            
        if is_below_zero:
            reversed_num *= -1
            
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num