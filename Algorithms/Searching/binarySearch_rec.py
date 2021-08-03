#Binary Search Recursive 

# Binary search algorithm
# only works for sorted arrays 

def binarySearch(array,leftIndex,rightIndex,toFind):
    # a =[1,2,3,4,5,6,7,8]
    # print(binarySearch(a,0,7,5))
    # 0 < 7
    # mid = 0 + (7 -0)//2 = 3
    # a[mid] = 4 < 5
    # left = 4 
    #a = [5,6,7,8]
    # repeat

    if leftIndex <= rightIndex:
        
        midIndex = leftIndex + (rightIndex - leftIndex)//2

        if array[midIndex]==toFind:
            return toFind
        elif array[midIndex]>toFind:
            return binarySearch(array,leftIndex,midIndex-1,toFind)
        else:
            return binarySearch(array,midIndex-1,rightIndex,toFind)
    return -1


a =[1,2,3,4,5,6,7,8]
print(binarySearch(a,0,7,5))