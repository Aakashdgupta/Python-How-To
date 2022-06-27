'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function fib(n) that takes in a number as an argument,
 the function should return the nth number of fibonacci sequence.

 the first and 2nd number of the sequence is 1 
 we add two previous terms to get nth term

 fib(n): 1,1,2,3,5,8,13,21,34.....


'''

def fib(n):
    if n<=2:return 1
    if n==0:return 0
    return fib(n-1) + fib(n-2)


print(fib(6))
print(fib(10))