# Selection sort implementation


def selectionSort(array):

    size = len(array)
    # looping through each element from 0 to size
    
    for step in range(size):

        # caching min index as initial index
        minindex = step
        # looping from step ( first time 0 ) to size
        for i in range(step, size):
            # if element at minindex is grater than element at i
            # update minimum index as i
            if array[minindex] > array[i]:
                minindex = i

            
        # at end of second loop
        # swap minimum value with first most element 
        # in sub array ( startimng from 0)

        array[step], array[minindex] = array[minindex], array[step]


ar = [4, 7, 9, 3, 0]
selectionSort(ar)
print(ar)
