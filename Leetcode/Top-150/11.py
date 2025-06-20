class Solution:
    def maxArea(self, height):
        l, r = 0, len(height)-1
        maxarea = 1
        while l < r:
            if height[l] < height[r]:
                area = min(height[l], height[r]) * (r-l)+1
                l+=1
            elif height[r] < height[l]:
                area = min(height[l], height[r]) * (l-r) +1
                r-=1
            else:
                if height[l+1] > height[r-1]:
                    area = height[l] * (l-r) +1
                    r-=1
                else:
                    area = height[r] * (l-r) +1
                    l += 1
            
            maxarea = max(area, maxarea)
        
        return maxarea

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))


             
