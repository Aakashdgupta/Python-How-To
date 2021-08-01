class node:
    def __init__(self):
        self.prev = None
        self.data = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        n = node()
        n.data = value

        if self.head == None:
            self.head = n

        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = n


    def insert(self,value):
        n = node()
        n.data =value

        self.head.prev = n
        n.next = self.head
        self.head = n

    def insertAfter(self,value,after):

        n = node()
        n.data = value

        temp = self.head
        while temp:
            if temp.data == after:

                n.prev =temp
                temp.next.prev = n
                n.next = temp.next
                temp.next = n
            
            temp = temp.next

    def delete(self,value):
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
        else:
            temp = self.head

            while temp:
                prev = temp.prev
                nex = None if temp.next ==None else temp.next

                if temp.data == value:
                    prev.next = nex
                    if nex:
                        nex.prev = prev
                       
    def priintDLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    dll = DoublyLinkedList()
    print(" Appended 1")
    dll.append(1)
    print(" Appended 6")
    dll.append(6)
    print(" Appended 4")
    dll.append(4)
    print(" Inserted 0")
    dll.insert(0)
    print(" Inserted  2 after 0")
    dll.insertAfter(2, 0)
    print("deleted 0")
    dll.delete(0)
    print("all items in Doubly Linked list")
    dll.priintDLL()
