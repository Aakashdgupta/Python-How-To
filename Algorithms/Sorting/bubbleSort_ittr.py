
# Bubble sort algorithm implementation 
# bubble sort algorith takes an array 
# and compares first two item 
# if first item is larger than second 
# its out of order 
# hence swaps these to values 
# repeats these steps till length of the array 
# a variable swapped is used to optimize the algorith
# if in any phase there is no swapping it means 
# array got sorted and its time to break loop
def bubbleSort(array):
    length = len(array)
    for i in range(length):
        swapped = False

        for j in range(0,length-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
            
        if swapped == False:
            break
    

			
arr =[64,34,25,12,22,11,90]
bubbleSort(arr)
print(arr)