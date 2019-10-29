#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # new = ""
        split = s.split()
        # for letter in split:
        #     new = letter + " " + new
        # new = new.rstrip()
        # return new

        split_list_reversed = split[::-1]
        # print(split_list_reversed)
        split_string = " ".join(split_list_reversed)
        # print(split_string)
        return split_string

        
# @lc code=end

