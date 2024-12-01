nums = [0,1,0,3,12]
l, r = 0,1

while r < len(nums):
    if nums[l] == 0 and nums[r]!=0:
        nums[l], nums[r] = nums[r], nums[l]
    l+=1
    r+=1
print(nums)


# left = 0
#     for right in range(len(nums)):
#         if nums[right] !=0:
#             nums[right], nums[left] = nums[left], nums[right]
#             left +=1