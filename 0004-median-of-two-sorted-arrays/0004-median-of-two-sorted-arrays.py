class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        left, right = 0, m

        while left <= right:
            partition_x = (left + right) // 2
            partition_y = (m + n + 1) // 2 - partition_x

            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (m + n) % 2 == 0:
                    median = (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    median = max(max_left_x, max_left_y)
                return median
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1

        return 0