class node:
    def __init__(self):
        self.data = None
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        # INSERT DATA AT START

        # 1 Create a new node
        n = node()

        # 2 Insert data
        n.data = value

        # 3 Check if list is empty
        if self.head == None:

            #  if so set n as head
            self.head = n

        else:
            # if not
            n.next = self.head
            self.head = n

    def append(self, value):

        # INSERT DATA AT END

        # 1 create new node
        n = node()
        n.data = value

        # 2 check if list is empty
        # if so set head of list to n
        if self.head == None:
            self.head = n

        else:
            #  3 loop through the list to get last node
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = n

    def insertAfter(self, after, value):
        # 1 craete new node
        n = node()
        n.data = value

        temp = self.head
        while temp:
            if temp.data == after:
                n.next = temp.next
                temp.next = n

            temp = temp.next

    def priintLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete(self, value):
        # 1 Create two temporary variable 
        # first which holds head of list
        # second which holds link of heads value

        first = self.head
        second = first.next

        # 2 check if head is the item to be deleted 
        # if so set the head to its next value 
        # which results in deletion oh head automatically

        if self.head.data == value:
            self.head = self.head.next


        # 3 else loop through list to find 
        # item to be deleted using second 
        # to delete it set firsts link( second) 
        # to seconds link 
        # which deletes sercond value 
        else:
            while second:
                if second.data == value:
                    first.next = second.next

                first = first.next
                second = second.next


if __name__ == '__main__':
    l = linkedList()

    l.insert(3)
    print(" Inserted 3")
    l.insert(4)
    print(" Inserted 4")
    l.append(5)
    print(" appended 5")
    l.insertAfter(3, 6)
    print(" inserted 6 after 3")

    print(" Printing all items ")
    l.priintLL()

    print()
    print("deleted 6")
    l.delete(6)

   
    print(" Printing all items ") 
    l.priintLL()
