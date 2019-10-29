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
        split_list_reversed = split[::-1]
        # print(split_list_reversed)
        split_string = " ".join(split_list_reversed)
        # print(split_string)
        return split_string[::-1]

        
        # for letter in split:  # traverse each word in words
        #     new = letter + " " + new
        # new = new.rstrip()
        # print(new)
        # return "".join(new[::-1]) 

# @lc code=end

