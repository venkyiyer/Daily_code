n1 = [3,2,3]
result , count = 0,0

for i in n1:
    if count == 0:
        result = i
    count += (1 if i == result else -1)

print(result)