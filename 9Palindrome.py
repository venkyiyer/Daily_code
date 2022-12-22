class solution:

    def palindrome(self, x):
        original = x
        new_num = 0
        while x > 0:
            new_num = new_num * 10 + x%10
            x = x//10
        return new_num == original

obj = solution()
obj.palindrome('123')