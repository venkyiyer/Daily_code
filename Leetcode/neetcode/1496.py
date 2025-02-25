path = "NES"

class Solution:
    def isPathCrossing(self, path):
        d={'N':[0,1], 'S':[0,-1], 'E':[1,0], 'W':[-1,0]}
        visit = set()
        x, y = 0,0
        for i in path:
            visit.add((x,y))
            dx, dy = d[i]
            x, y = x+dx, y + dy
            if (x,y) in visit:
                return True
        
        return False

obj = Solution()
print(obj.isPathCrossing(path))