#Insertion sort Algorithm


def insertionSort(array):
    for i in range(1,len(array)):
        #[6,3,7,1,12,10]

        # i = 1
        # key = 3
        # j = i - 1 = 0 
        # j = 0  and 3 < 6
        #now 6 is trored in place of 3
        #j = -1
        #loop brakes
        # and 3 is stored in place of 6
        #[3,6,7,1,12,10]


        # i = 2
        # key = 7
        # j = 2 -1 = 1
        # j = 1 and 7 not < 6
        # while loop continues 
        # 7 is stored in place of 7
        #[3,6,7,1,12,10]

        # i = 3
        # key = 1
        # j = 3 -1 = 2
        # j = 2 and 1  < 7
        # 7 is stored in place of 1 
        #[3,6,7,7,12,10]

        # j decreased by 1 = 1
        # 6 is stored in place of 7
        #[3,6,6,7,12,10]
        # j is decreased by 1 = 0
        # 3 is stored in place of 6
        #[3,3,6,7,12,10]
        # j is decreased by 1 = -1
        # while loop breaks 
        # 1 is stored in place of 3
        #[1,3,6,7,12,10]
        #process repeated ...



        key = array[i]

        j = i - 1

        while j>= 0 and key < array[j]:
            
            array[j+1] = array[j]   
            j -= 1
        array[j+1] = key


arr = [6,3,7,1,12,10]
insertionSort(arr)
print(arr)