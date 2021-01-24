from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1 暴力
        # for i in matrix:
        #     if target in i:
        #         return True
        # return False
        
        if not matrix or not matrix[0]:
            return 
        left, right = 0, len(matrix) * len(matrix[0])-1
        arr = [column for row in matrix for column in row]
        while left <= right:
            mid = ((right - left) >> 1) + left
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1  # ascending
            else:
                right = mid - 1
        return False



print(Solution().searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],target=3))
print(Solution().searchMatrix(matrix=[[1,3]],target=3))