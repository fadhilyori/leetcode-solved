class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        nums3 = [None] * (m + n)
        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3[k] = nums1[i]
                i += 1
            else:
                nums3[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums3[k] = nums1[i]
            k += 1
            i += 1

        while j < n:
            nums3[k] = nums2[j]
            k += 1
            j += 1

        return nums3
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = self.merge(nums1, nums2)
        n = len(nums3)
        mid = n // 2

        if n % 2 == 0:
            median = (nums3[mid - 1] + nums3[mid]) / 2
        else:
            median = nums3[mid]

        return median