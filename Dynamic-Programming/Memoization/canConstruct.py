'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function canConstruct(targetstr,strlist) that takes
in a target String  and an list of strings as arguments.
the function should return a boolean indicating whether 
or not it is possible to generate the target str using 
string from the array

'''



def canConstruct(targetStr,listStr):
    if len(targetStr)==0 :return True

    for word in listStr:
        try:
            if targetStr.index(word)==0:
                newstr = targetStr.removeprefix(word)
                if canConstruct(newstr,listStr):
                    return True
        except(ValueError):
            pass
    return False


def canConstructOptimized(targetStr,listStr,memo={}):
    if targetStr in memo : return memo[targetStr]
    if len(targetStr)==0 :return True

    for word in listStr:
        try:
            if targetStr.index(word)==0:
                newstr = targetStr.removeprefix(word)
                if canConstructOptimized(newstr,listStr):
                    memo[targetStr]=True
                    return True
        except(ValueError):
            pass
    memo[targetStr]=False
    return False

print(canConstruct("abcdef",["ab","cd","ef"]))
print(canConstruct("abcdef",["abcd","cd","efg"]))
print(canConstructOptimized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
["e","ee","eee","eeee","eeeee"]))
