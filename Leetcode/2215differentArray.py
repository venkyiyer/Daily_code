class Solution:
    def findDifference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        res1 = set()
        res2 = set()

        for i in nums1:
            if i not in nums2:
                res1.add(i)
        
        for j in nums2:
            if j not in nums1:
                res2.add(j)
        
        return list(res1), list(res2)

obj = Solution()
print(obj.findDifference([1,2,3], [2,4,6]))