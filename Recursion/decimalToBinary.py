'''
PROGRAM TO CONVERT GIVEN DECIMAL NUMBER TO 
BINARY USING RECURSION
'''


def DecimalToBinary(decimal, result=[]):
    if decimal == 0:
        return result
    result.append(decimal % 2)
    return DecimalToBinary(decimal//2, result)


binary = DecimalToBinary(234)


def revArrayAsStr(arr):
    l = len(arr) - 1
    while l >= 0:
        print(arr[l], end='')
        l -= 1



revArrayAsStr(binary)