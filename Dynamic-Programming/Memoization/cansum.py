'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function cansum(targetsum,numbers) that takes
in a target sum and an array of numbers as arguments.
the function should return a boolean indicating whether 
or not it is possible to generate the target sum using 
numbers from the array

'''


def cansum(targetsum, numbers):
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for num in numbers:
        remainder = targetsum-num
        if (cansum(remainder, numbers)) == True:
            return True
    return False


def cansumOptimized(targetsum, numbers, memo={}):
    if str(targetsum) in memo:
        return memo[str(targetsum)]
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for num in numbers:
        remainder = targetsum-num
        if cansumOptimized(remainder, numbers) == True:
            memo[str(targetsum)] = True
            return memo[str(targetsum)]
    memo[str(targetsum)] = False
    return memo[str(targetsum)]


print(cansum(7, [2, 3]))
print(cansumOptimized(301, [2 , 5]))
