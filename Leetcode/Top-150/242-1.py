class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t)

obj = Solution()
print(obj.isAnagram(s = "jar", t = "jam"))