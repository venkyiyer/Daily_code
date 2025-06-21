class Solution:
    def maxArea(self, height):
        l, r = 0, len(height)-1
        maxarea = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxarea = max(area, maxarea)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return maxarea

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))


             
