from collections import Counter
class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)
        nums.sort(key = lambda n: (count[n], -n))

        return nums

obj = Solution()
print(obj.frequencySort([-1,1,-6,4,5,-6,1,4,1]))
