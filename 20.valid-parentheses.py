#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        valids = ("()", "[]", "{}")
        while s:
            if len(s) % 2 != 0:
                return False
            for valid in valids:
                if valid in s:
                    s = s.replace(valid, "")
                    break
            else:
                return False
        return True


# @lc code=end
