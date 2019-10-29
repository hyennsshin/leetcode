#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        new = ""
        split = s.split()   # split the words
        for letter in split:  # traverse each word in words
            new = letter + " " + new
        new = new.rstrip()
        print(new)
        return "".join(new[::-1]) 
               
# @lc code=end

