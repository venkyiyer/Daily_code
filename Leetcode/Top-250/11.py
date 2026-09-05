class Solution:
    def maxArea(self, height):
        l,r,res = 0, len(height)-1, 0

        while l<r:
            area = (r - l) * min(height[l], height[r])
            res = max (res, area)
            if height[l] < height[r]:
                l +=1
            else: 
                r -=1
        return res

obj = Solution()
print(obj.maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))