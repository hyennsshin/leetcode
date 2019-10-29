#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        new = ""
        split = s.split()
        for letter in split:
            new = letter + " " + new
        new = new.rstrip()
        return new

        
# @lc code=end

