class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in num_dict:
                return [num_dict[m], i]
            num_dict[n] = i
        return []