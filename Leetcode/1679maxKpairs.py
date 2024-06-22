from collections import Counter
class Solution:
    def maxOperations(self,nums, k):
        c = Counter(nums)
        output =0
        seen = set()
        for x in c:
            if x not in seen and (k-x) in c:
                if x == (k-x):
                    output += c[x]//2
                else:
                    output += min(c[x], c[k-x])
                seen.add(x)
                seen.add(k-x)

        return output

obj = Solution()
print(obj.maxOperations([1,2,3,4], k = 6))