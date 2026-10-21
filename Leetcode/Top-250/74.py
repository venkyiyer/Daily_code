class Solution:
    def searchMatrix(self, matrix, target):
        ROWS, COLUMN = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS- 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = mid + 1
            else: 
                break

        if not (top<= bottom):
            return False
        mid = (top + bottom) // 2
        l, r = 0, COLUMN -1 
        while l <=r:
            m = (l+r)//2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                l = m - 1
            else:
                return True
        return False

obj = Solution()
print(obj.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) 
