#  isPrime(x) returns True if passed number is prime else false




def isPrime(x):
    divisionCount =0
    for i in range(1,x+1):
        if x%i==0:
            divisionCount +=1
        
    if divisionCount<=2:
        return True
    
    return False


# isEven(x) returns True if x is a Even number else returns false

def isEven(x):
    return x%2==0


# isOdd(x) returns True if x is a Odd number else returns false

def isOdd(x):
    return x%2 != 0


def countDigitsIn(x):
    count =0

    while x>0:
        x= x//10
        count +=1
    
    return count

def sumOfDigitsIn(x):
    sum =0

    while x>0:
        sum += x%10
        x = x//10
    return sum

def productsOfDigitsIn(x):
    product = 1

    while x>0:
        product *= x%10
        x = x//10
    return product





def reverseOf(x):
    rev =0
    while x>0:
        rem = x%10
        rev = rev * 10 + rem
        x = x//10
    
    return rev

'''
In NUMBER THEORY PALINDROME ARE NUMBERS WHOES REVERSE IS NUMBER ITSELF
EX 121 
'''
def isPalindrome(x):
    return reverseOf(x) ==x

'''
ARMSTRONG NUMBER EX 407 = 4*4*4 + 0*0*0 + 7*7*7 = 407
'''
def isArmstrong(x):
    temp = x
    digit_count =countDigitsIn(x)
    sum = 0

    while x>0:
        sum += (x%10) **digit_count
        x = x //10
    
    return temp == sum

'''
IN NUMBER THEORY PERFECT NUMBER IS A NUMBER WHOES SUM OF DIVISORS 
EXCLUDING IT SELF IS EQUAL TO ORIGINAL NUMBER
'''
def isPerfect(x):
    sum = 0
    
 
    for i in range(1,x):
        if x%i==0: sum += i
    
    return sum ==x

'''
IN NUMBER THEORY A NUMBER IS A HARSHAD NUMBER IF NUMBER IS PERFECTLY 
DIVISIBLE BY SUM OF ITS DIGITS 
171 , 1+7+1 = 9
171%9 ==0
'''
def isHarshad(x):
    sum = sumOfDigitsIn(x)
    return x%sum == 0

'''
IN NUMBERS THEORY ABUNDANT NUMBER IS A NUMBER WHOES SUM OF DIVISORS 
IS GREATER THAN NUMBER ITSELF'''

def isAbundant(x):
    sum =0
    for i in range(1,x):
        if x%i==0: sum += i
    return sum>x

'''
IN NUMBER THEORY AUTOMORPHIC NUMBER IS A NUMBER WHOES
SQUARE ENDS IN NUMBER ITSELF EX 5 , 5*5 = 25 ENDS WITH 5 '''

def isAutomorphic(x):
    sqr = x*x
    return (sqr-x) %10 ==0



""""
IN NUMBERS THEORY A NEON NUMBER IS A NUMBER WHOES SQUARE'S  SUMS OF DIGITS
IS EQUAL TO NUMBER IT SELF EX 9 , SQUARE OF 9 = 81 , 8+1 =9 """

def isNeon(x):
    sqr = x*x
    sum = sumOfDigitsIn(sqr)
    return sum==x

'''
IN NUMBERS THEORY A SPY NUMBER IS A NUMBER WHOES SUM OF DIGITS 
IS EQUAL TO PRODUCT OF DIGITS '''

def isSpy(x):
    return sumOfDigitsIn(x) == productsOfDigitsIn(x)

def isLeapYear(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False