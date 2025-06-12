# class Solution:
#     def topKfrequent(self, nums, k):
#         d = {}
#         freq = [[] for i in range(len(nums)+1)]

#         for n in nums:
#             d[n] = 1 + d.get(n, 0)
        
#         for n, c in d.items():
#             freq[c].append(n)
        
#         res = []
#         for i in range(len(freq)-1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res

from collections import Counter

class Solution:
    def topFrequentelements(self, nums, k):
        count_of_elements = Counter(nums)
        l = []
        for ele in count_of_elements:
            if count_of_elements[ele] >=k:
                l.append(ele)
        
        return l

obj = Solution()
print(obj.topFrequentelements(nums=[1], k=1))