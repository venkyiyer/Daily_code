class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        l =[]
        for n in nums: 
            if n in d: 
                d[n]+=1
            else:
                d[n]=1
        l = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        return l[:k]

obj = Solution()
print(obj.topKFrequent(nums = [1], k = 3))