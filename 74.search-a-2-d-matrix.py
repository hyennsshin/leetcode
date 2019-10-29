#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False
        
        count = 0
        end = row * col - 1
        while count <= end:
            pivot_idx = (count + end) // 2
            pivot_element = matrix[pivot_idx // col][pivot_idx % col]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    end = pivot_idx - 1
                else:
                    count = pivot_idx + 1
        return False
        
# @lc code=end

