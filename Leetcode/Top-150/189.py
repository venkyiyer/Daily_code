nums = [1,2,3,4,5,6,7]
k = 3

for i in range(len(nums)-1):
    if i <= k:
        print(nums[i])
        nums[i+k] = nums[i]
    else:
        n = (i+k)% len(nums)
        nums[n] = nums[i]

print(nums)