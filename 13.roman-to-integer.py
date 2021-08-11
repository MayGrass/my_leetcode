#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def __init__(self):
        self.roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            try:
                total = (
                    total + self.roman_numerals[s[i]]
                    if self.roman_numerals[s[i]] >= self.roman_numerals[s[i + 1]]
                    else total - self.roman_numerals[s[i]]
                )
            except:
                total += self.roman_numerals[s[i]]
        return total


# @lc code=end
