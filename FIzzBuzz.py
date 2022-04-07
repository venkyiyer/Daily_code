class Solution:
    def fizzBuzz(self, n: int):
        for i in range(1,n):
            print(i)
            if i % 3 and i % 5  == 0:
                i = 'FizzBuzz'
            elif i% 3 == 0:
                i == 'Fizz'
            elif i % 5 == 0:
                i == 'Buzz'
            else:
                return n
        return n 

obj = Solution()
print(obj.fizzBuzz(3))