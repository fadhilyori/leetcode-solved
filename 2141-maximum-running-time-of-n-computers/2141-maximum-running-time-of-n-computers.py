class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check_feasibility(target):
            extra = sum(min(power, target) for power in batteries)
            return extra // n >= target
        
        left, right = 1, sum(batteries) // n + 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if check_feasibility(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1
        