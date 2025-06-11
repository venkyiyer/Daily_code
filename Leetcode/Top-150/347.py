class Solution:
    def topKfrequent(self, nums):
        d = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        for n, c in d.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        