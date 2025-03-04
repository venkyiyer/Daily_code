paths = [["B","C"],["D","B"],["C","A"]]

class Solution:
    def destCity(self, paths):
        s = set()
        for i in paths:
            s.add(i[0])
        
        for i in paths:
            if i[1] not in s:
                return i[1]

obj = Solution()
print(obj.destCity(paths))
