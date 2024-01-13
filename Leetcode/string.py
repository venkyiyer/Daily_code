# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         calc={}
#         longest = []
#         for index, alphabet in enumerate(s):
#             if alphabet in calc:
#                 calc[alphabet]+=1
#                 if calc[alphabet] > 1:
#                     longest.append(index)
#             else:
#                 calc[alphabet]= 1
            
#         return max(longest)

# obj = Solution()
# obj.lengthOfLongestSubstring('abcabcbb')


# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# dict= {}

# for so, ix in zip(s, indices):
    
# a=[1,[2,3],4,5]
# result = lambda x: list(map(lambda y:2*y, x)) if isinstance(x,list) else lambda x:3*x
# print(result(a))


# s = "K1:L2"
# s1 = s.split(':')
# l = []
# for i in range(ord(s[0]), ord(s[3])+1):
#     for j in range(int(s[1]), int(s[4])+1):
#         l.append(chr(i)+str(j))

# print(l)

# r = {}
# s = "RLRRLLRLRL"
# for i in s:
#     if i in r:
#         r[i] +=1
#     else:
#         r[i] =1
    

# print(sum(r.values())//2)
# count_r = 0
# count_l = 0
# count = 0
# for i in s:
#     if i == 'R':
#         count_r +=1
#     else:
#         count_l +=1
#     if count_l == count_r:
#         count+=1

# print()


# key = 'eljuxhpwnyrdgtqkviszcfmabo'
# message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# t = {}
# s = []
# ascii_value = 97
# for i in key: 
#     t[i] = ascii_value
#     ascii_value +=1

# for j in message:
#     if j == ' ':
#         s.append(' '.join(j))
#     else:
#         chars = t[j]
#         alphabet = chr(chars)
#         s.append(''.join(alphabet))

# x = ''.join(s)
# print(x)




# print(l)

# s = "is2 sentence4 This1 a3"
# words = s.split(' ')
# new_list = [0]*len(words)
# for i in words:
#     new_list[int(i[-1])-1] = i[:-1]
# _list = ' '.join(new_list)

# print(_list)


# sentence = "thequickbrownfoxjumpsoverthelazydog"

# l = [x for x in range(97,123)]
# print(l)
# # for s in range(len(sentence)):


# sentence = "thequickbrownfoxjumpsoverthelazydog"

# l = [x for x in range(97,123)]
# print(l)
# # for s in range(len(sentence)):
# if int(0) in l:
#     print('jasd')

# class student: 
#     def __init__(self): 
#         '''The student class is initialized'''

#     def print_student(self): 
#         '''Returns the student description'''
#         print('student description') 

# help(student)


# nums  = [5,0,1,2,3,4]

# # print(nums[nums[1]])
# # l = []
# # for i in range(len(nums)):
# #     l.append(nums[nums[i]])

# # print(l)

# q = len(nums)
# for i,c in enumerate(nums):
#     nums[i] += q * (nums[c] % q)
# for i,_ in enumerate(nums):
#     nums[i] //= q
  

# nums = [1,2,1]
# q = []

# nums.extend(nums)
# print(nums)

# nums = [1,2,3,4]
# sum = 0
# l = []

# for i in nums:
#     l.append(sum + i)
#     sum = sum + i

# print(l)
# nums = [2,5,1,3,4,7]
# n = 3

# for i in range(0,n):
#     for j in range(n, len(nums)-1):
#         nums[i], nums[j] = nums[j], nums[i]

# print(nums)

nums = [1,2,3,1,1,3]
my_count = 0
my_dict = {}

for n in nums:
    # Check to see if number has already been encountered
    if n in my_dict:
        # Increase count by the number of previous instances
        my_count += my_dict[n]

        # Increase the count of previous observation
        my_dict[n] +=1
    else:
        # Store newly encountered number along with its count
        my_dict[n] = 1
        
# return my_count
