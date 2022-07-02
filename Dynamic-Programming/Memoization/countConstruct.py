'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function countConstruct(targetstr,strlist) that takes
in a target String  and an list of strings as arguments.
the function should return a integer indicating exactly
in how many ways it is possible to generate the target str using 
string from the array otherwise return 0

'''

def countConstruct(targetStr,listStr):
    if len(targetStr) ==0: return 1
    count =0

    for word in listStr:
        try:
            if targetStr.index(word)==0:
                newstr = targetStr.removeprefix(word)
                way = countConstruct(newstr,listStr)
                count +=way
        except(ValueError):
            pass
    return count


print(countConstruct("abcdef",["ab","cd","ef","abcd","re","abc","def"]))