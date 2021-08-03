def shellSort(arr):

    size = len(arr)
    interval = size//2

    # rearrang elements at each interval
    # n/2 , n/4, n/8.....
    # loop till interval becomes 0
    # example if size of array is 8
    # intervals = 4,2,1
    while interval > 0:

        # loop from interval till size
        # example if array size is 8
        # loop through 4 to 8

        for i in range(interval, size):
            # initially temp = element at interval position
            #  ex 4
            temp = arr[i]
            # initially j is also interval = 4
            j = i
            while j >= interval and arr[j-interval] > temp:
                # loop untill j greater than  or equal interval
                # here both is 4
                # and arr[4-4] = arr[0] > arr[4]
                # save arr[j-interval] here arr[0] at arr[j] here arr[4]
                arr[j] = arr[j-interval]
                # decrease j by interval
                j -= interval

            # sace initial key value to j th place

            arr[j] = temp
        # update interval
        interval //= 2


arr = [12, 34, 54, 2]
shellSort(arr)
print(arr)
