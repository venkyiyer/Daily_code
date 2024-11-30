haystack = "sadbutsad"
needle = "sad"

i, count = 0, 0

for r in range(len(needle)):
    if needle[r] == haystack[r]:
        while r < len(needle):
            if needle[r] == haystack[r]:
                count+=1
        if count == len(needle):
            print(r)
    print(-1)