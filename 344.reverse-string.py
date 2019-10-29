#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        i = 0
        while j > i:
            s[j], s[i] = s[i], s[j]
            j -= 1
            i += 1

        
# @lc code=end

