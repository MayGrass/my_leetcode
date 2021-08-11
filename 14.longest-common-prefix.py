#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(set(strs))  # 去重複
        if len(strs) == 1:  # 陣列只有一個東西直接回傳
            return strs[0]
        shortest = min(strs, key=len)
        strs.remove(shortest)  # 自己不需要重新比對
        for index, single_text in enumerate(shortest):
            for other in strs:
                if other[index] != single_text:
                    return shortest[:index]
            if shortest == 1 and other[index] == single_text:
                return shortest
        return shortest


# @lc code=end
