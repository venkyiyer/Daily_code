from collections import Counter

class Solution:
    def anagram(self, st1, st2):
        c1= Counter(st1.lower())
        c2 = Counter(st2.lower())
        if c1!=c2:
            return False
        else:
            return True

obj = Solution()
print(obj.anagram('rat', 'car'))