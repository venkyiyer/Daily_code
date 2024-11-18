nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

indexofzeros = []
for i in range(len(nums1)):
    if nums1[i] == 0:
        indexofzeros.append(i) 

if len(indexofzeros)>0:
    for j in range(len(indexofzeros)):
        nums1[indexofzeros[j]] = nums2[j]
    print(sorted(nums1))
else:
    print(nums1)


# print(indexofzeros)
# print(sorted(nums1))

# last = m + n -1
#         while m > 0 and n>0:
#             if nums1[m-1] > nums2[n-1]:
#                 nums1[last] = nums1[m-1]
#                 m-=1
#             else:
#                 nums1[last] = nums2[n-1]
#                 n -= 1
#             last -= 1
#         while n >0:
#             nums1[last] = nums2[n-1]
#             n, last = n-1, last - 1