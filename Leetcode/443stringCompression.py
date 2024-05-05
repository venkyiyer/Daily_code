class Solution:
    def compress(self, chars):
        get_numbers = {}
        make_list = []
        for i in chars:
            if i not in get_numbers:
                get_numbers[i]=1
            else:
                get_numbers[i] +=1

        for k, v in get_numbers.items():
            if v == 1:
                make_list.append(k)
            elif len(v)==2:
                make_list.append(k)
                make_list.extend([int(x) for x in str(v)])

        print(make_list)

obj = Solution()
obj.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
