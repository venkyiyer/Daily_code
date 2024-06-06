from collections import defaultdict
class Solution:
    def equalpairs(self, grid):
        row_counts = defaultdict(int)
        count = 0

        for row in grid:
            row_counts[tuple(row)] +=1
        
        for column in zip(*grid):
            count += row_counts[column]

        return count 

obj = Solution()
print(obj.equalpairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

