class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row) - 1

                while left <= right:   
                    mid = left + (right - left) // 2

                    if target == row[mid]:
                        return True
                    elif target < row[mid]:
                        right = mid - 1
                    elif target > row[mid]:
                        left = mid + 1
        return False
