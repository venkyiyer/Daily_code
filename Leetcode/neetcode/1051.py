class Solution:
    def heightChecker(self, heights):
        count = [0]*101
        for h in heights:
            count[h] +=1
        expected = []
        for h in range(1, 101):
            c = count[h]
            for _ in range(c):
                expected.append(h)
        res = 0
        for i in range(len(heights)):
            if heights[i]!= expected[i]:
                res +=1
        
        return res

obj = Solution()
print(obj.heightChecker([1,1,4,2,1,3]))