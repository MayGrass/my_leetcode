#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 數字陣列不能用join，把陣列裡每個數字都轉成字串join起來後+1
        number = int("".join(str(digit) for digit in digits)) + 1
        return [int(i) for i in str(number)]


# @lc code=end
