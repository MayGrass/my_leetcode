#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, one in enumerate(nums):
            for index2, two in enumerate(nums):
                if index1 == index2:
                    continue
                elif one + two == target:
                    return [index1, index2]
# @lc code=end

