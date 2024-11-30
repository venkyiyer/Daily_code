haystack = "sadbutsad"
needle = "sad"

if needle == "":
    print(0)

for i in range(len(haystack) + 1 - len(needle)):
    print(haystack[i:i+len(needle)])
    if haystack[i:i+len(needle)] == needle:
        print(i)
print(-1)