class Solution:
    def sortPeople(self, names, heights):
        return [name for _, name in sorted(zip(heights, names), reverse= True)]

obj = Solution()
print(obj.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))