#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:       
        rom_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        val = 0
        pre_val = 0
        answer = 0
        for letter in s:
            val = rom_to_int[letter]
            answer += val
            if val > pre_val:
                answer -= pre_val*2
            pre_val = val   
        return answer
        
# @lc code=end

