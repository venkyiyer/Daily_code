class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        l, r = 0, len(nums)-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        # return nums

        l = 0
        r = k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        l = k
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1


        return nums

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], k=2))
        