def recursiveMethod(n):
    if n < 1:
        print('Execution is finished')
    else:
        recursiveMethod(n-1)
        print("-->",n)

recursiveMethod(4)