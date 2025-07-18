class Solution:
    def mergeArrays(self, nums1, nums2):
        d = {}
        for i in nums1:
            d[i[0]] = i[1]
        for j in nums2:
            if j[0] in d:
                d[j[0]] += j[1]
            else:
                d[j[0]] = j[1]
        l = [[k,v] for k, v in d.items()]
        return sorted(l)

obj = Solution()
print(obj.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))