class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            hl = height[left]
            hr = height[right]
            
            min_height = min(hl, hr)
            
            area = min_height * (right - left)
            
            # print(left, right, hl, hr, min_height, length, area)
            
            max_area = max(area, max_area)
                
            if hl < hr:
                left += 1
            else:
                right -= 1
            
        return max_area