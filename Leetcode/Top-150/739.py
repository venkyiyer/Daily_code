class Solution:
    def dailyTemperature(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        
        return res

obj = Solution()
print(obj.dailyTemperature([73,74,75,71,69,72,76,73]))
