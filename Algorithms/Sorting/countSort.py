

def countSort(array):
    # creating output array ( now containing 0)
    # as same lenth as original array is
    output = [0 for i in range(len(array))]
    # creating count array to contain occurance of
    # each item in original array / 256 possible unicode
    # chracters
    count = [0 for i in range(256)]

    # counting occourance
    # ord function returns equivalence
    # unicode for a string chracter
    # exa for 'a' it will return 97
    # hence item at 97th index is 0 , will become 1
    for i in array:
        count[ord(i)] += 1

    # adding actual count of each item with its previus 
    # items count
    for i in range(256):
        count[i] += count[i-1]

    # as we know in count array 
    # we are storing occurance of each item 
    # in items unicode position 
    # example if 'a' ( unicode 97) occurs 1 = times 
    # count[97 -1 ] will be 1( occurs 1 times)
    # considering this in mind 
    # we use this occurance value as position index 
    # for output array to store respective item 
    # here 'a' will go to output[1] = 'a'
    # at last we decrease occurance count by 1
    # here 1 becomes 0 
    # which means next time if we find 'a' it will go to
    # output[0] = 'a'


    for i in range(len(array)):
        output[count[ord(array[i])]-1] = array[i]
        count[ord(array[i])] -= 1

    return output




ans = countSort("5h8k")
ans = "".join(ans)
print(ans)
