ops = ["5","2","C","D","+"]

class Solution:
    def calPoints(self, ops):
        stck = []
        for op in ops:
            if op == "+":
                stck.append(stck[-1] + stck[-2])
            elif op == "D":
                stck.append(2*stck[-1])
            elif op == "C":
                stck.pop()
            else:
                stck.append(int(op))
            
        return sum(stck)

obj = Solution()
print(obj.calPoints(ops))