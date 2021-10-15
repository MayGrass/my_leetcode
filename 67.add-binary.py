#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 轉成整數想加後轉回二進制純字串，再去掉字首0b
        return bin(int(a, 2) + int(b, 2))[2:]


# @lc code=end
