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