students = [1,1,0,0]
sandwiches = [0,1,0,1]
from collections import Counter
class Solution:
    def countStudents(self, students, sandwiches):
        res = len(students)
        cnt = Counter(students)
        for s in sandwiches:
            if cnt[s] >0:
                res-=1
                cnt[s] -=1
            else:
                return res
        
        return res

obj = Solution()
print(obj.countStudents(students, sandwiches))
        