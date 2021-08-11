#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
import math


class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x >= 0 else -int(str(abs(x))[::-1])
        if math.pow(-2, 31) <= result <= math.pow(2, 31) - 1:
            return result
        else:
            return 0


# @lc code=end
