'''

PROGRAM TO SUM NUMBERS FROM 0 TO N USING RECURSION
'''


def sumN(n):
    if n == 0:
        return n
    return n + sumN(n-1)


print(sumN(10))
