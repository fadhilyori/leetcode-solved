class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_batteries = sum(batteries)
        left, right = 1, total_batteries // n + 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            extra = sum(min(power, mid) for power in batteries)
            
            if extra // n >= mid:
                left = mid + 1
            else:
                right = mid
        
        return left - 1
        