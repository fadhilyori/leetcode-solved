class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        is_below_zero = True if x < 0 else False
        x = x if not is_below_zero else x * -1
        
        while x > 0:
            a = x % 10
            yt = y * 10 + a
            if -math.pow(2,31) > yt * -1 if is_below_zero else yt > math.pow(2,31) - 1:
                return 0
            y = yt
            x = x // 10

        return y * -1 if is_below_zero else y