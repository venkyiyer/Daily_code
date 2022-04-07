class Solution:
    def intersect(self, nums1, nums2):
        result1 = set(nums1)
        result2 = set(nums2)
        return list(result1 & result2)

obj = Solution()
print(obj.intersect([1,2,2,1], [2,2]))