'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function bestsum(targetsum,numbers) that takes
in a target sum and an array of numbers as arguments.
the function should return an array containing the shortest 
combination of numbers that add up to exactly the target 
sum 
if there is a tie for the shortest combination , you may 
return any one of the shortest

'''

from math import remainder


def bestsum(targetsum,numbers):
    if targetsum == 0 :return []
    if targetsum <0: return None

    best = None

    for n in numbers:
        remainder =targetsum - n
        x =bestsum(remainder,numbers)
        if x != None:
            x.append(n)
            if best == None: best =x
            if len(best) > len(x):
                best =x

    return best

def bestsumOptimized(targetsum,numbers,memo={}):
    if targetsum in memo:return memo[targetsum]
    if targetsum == 0 :return []
    if targetsum <0: return None

    best = None

    for n in numbers:
        remainder =targetsum - n
        x =bestsumOptimized(remainder,numbers,memo)
        if x != None:
            x.append(n)
            if best == None: best =x
            if len(best) > len(x):
                best =x
                return x
    res = memo[targetsum] = best
    return res 

    
print(bestsum(5,[2,3,5]))
print(bestsum(7,[2,3,5]))
print(bestsumOptimized(50,[2,3,5]))
    
