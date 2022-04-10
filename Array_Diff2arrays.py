class Solution:
    def findDifference(self, nums1, nums2):
        lst1 =[]
        lst2=[]
        nums1  = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i not in nums2:
                lst1.append(i)
        for j in nums2:
            if j not in nums1:
                lst2.append(j)
        return lst1, lst2

obj = Solution()
print(obj.findDifference([1,2,3,3],[1,1,2,2]))