#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 自己寫
        # compare_list = list()
        # while nums:
        #     temp, max_val = int(), nums[0]
        #     for num in nums:
        #         temp += num
        #         if temp > max_val:
        #             max_val = temp
        #     compare_list.append(max_val)
        #     del nums[0]
        # return max(compare_list)

        # 抄起來
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


# @lc code=end
