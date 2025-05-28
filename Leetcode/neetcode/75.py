class Solution:
    def sortColors(self, nums):
        l, r = 0, len(nums)-1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            # tmp = nums[i]
            # nums[i] = nums[j]
            # nums[j] = tmp
        
        while i <=r:
            if nums[i] == 0:
                swap(l,i)
                l +=1
            elif nums[i] ==2:
                swap(i, r)
                r -=1
                i-=1
            i+=1

        

obj = Solution()
print(obj.sortColors(nums = [2,0,2,1,1,0]))