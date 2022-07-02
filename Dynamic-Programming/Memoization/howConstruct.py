'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q write a function howConstruct(targetstr,strlist) that takes
in a target String  and an list of strings as arguments.
the function should return a list of strings indicating whether 
how it is possible to generate the target str using 
string from the array otherwise return None

'''


def howConstruct(targetStr,listStr):
    if len(targetStr)==0 :return []

    for word in listStr:
        try:
            if targetStr.index(word)==0:
                newstr = targetStr.removeprefix(word)
                li = howConstruct(newstr,listStr)
                if li != None:
                    li.append(word)
                    return li

        except(ValueError):
            pass
    return None


print(howConstruct("abcdef",["ab","cd","ef","abcd","re"]))
print(howConstruct("abcdef",["a","cd","bcd","abcd","ef"]))