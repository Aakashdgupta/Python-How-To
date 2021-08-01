'''
QUEUE IS A LINEAR DATASTRUCTURE , WHICH SIMULATES 
REALWORLD QUEUE PROGRAMATICALLY , IT REPRESENTS 
QUEUE OF ITEMS , WHERE NEW ITEMS CAN BE ENQUEUED AT REAR
POSITION , WHILE EXIST ITEMS CAN BE DEQUEUED FROM 
FRONT POSITION
'''

class queue:
    def __init__(self, lim=10):
        self.size = lim
        # alotting space statically
        self.q = [None] * self.size
        # front for getting data
        self.front = 0
        # reare for inserting data
        self.rear = 0

        self.total = 0

    # if total item is 0 queue is empty
    def isempty(self):
        return self.total == 0

    # if total item equals total limit queue is full
    def isfull(self):
        return self.total == self.size

    # enqueue to insert data in queue

    def enque(self, value):
        # if queue is not full
        if (self.isfull() == False):
            # insert item at curret rear index
            self.q[self.rear] = value
            # increase rear index
            # here its a circular increament
            self.rear = (self.rear + 1) % self.size
            # increase total item
            self.total += 1
        else:
            raise Exception('Queue overflow')
    # method to get data from queue

    def dequeue(self):
        # if only queue is not empty
        if(self.isempty() == True):
            raise Exception("Queue Underflow")
        else:
            # get data using front index
            temp = self.q[self.front]

            self.q[self.front] = None  # only for printing
            # increase front index
            self.front = (self.front + 1) % self.size
            # decrease total item
            self.total -= 1
            return temp

    def printQ(self):
        if self.isempty() == False:
            for i in self.q:
                if i:
                    print(i)


if __name__ == '__main__':
    q = queue()

    for i in range(9):
        q.enque(i)
        print("enqued", i)
        
    print("ITEMS in Queue =>")
    q.printQ()
    print()

    for i in range(9):
        print(" dequeued", q.dequeue())
