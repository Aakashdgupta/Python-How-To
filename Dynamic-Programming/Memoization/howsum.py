'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function howsum(targetsum,numbers) that takes
in a target sum and an array of numbers as arguments.
the function should return the array if  it is possible to generate the target sum using 
numbers from the passed array, other wise will return none

'''


def howsum(targetsum, numbers):
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    for num in numbers:
        remainder = targetsum - num
        x = howsum(remainder, numbers)
        if x != None:
            x.append(num)
            return x

    return None


def howsumOptimized(targetsum, numbers, memo={}):
    if str(targetsum) in memo:
        return memo[str(targetsum)]

    if targetsum == 0:
        return []
    if targetsum < 0:
        return None

    for num in numbers:
        remainder = targetsum - num
        x = howsumOptimized(remainder, numbers, memo)
        if x != None:
            x.append(num)
            memo[str(targetsum)] = x
            return x
    memo[str(targetsum)] = None
    return None


print(howsum(7, [2, 3]))
print(howsum(7, [5, 3,4,7]))
print(howsum(7, [2, 4]))
print(howsum(8, [2, 3,5]))
print(howsumOptimized(300, [7, 14]))
