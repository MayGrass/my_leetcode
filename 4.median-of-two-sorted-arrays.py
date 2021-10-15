#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        length = len(merged_list)
        median = length // 2
        if length % 2 == 0:
            return (merged_list[median - 1] + merged_list[median]) / 2
        else:
            return merged_list[median]


# @lc code=end
