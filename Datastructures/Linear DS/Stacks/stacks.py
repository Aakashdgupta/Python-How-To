'''
STACK IS A DATA STRUCTURE WHICH SIMULATES REAL WORLD
STACK IN PROGRAMMING , FOR EXAMPLE STACK OF BOOKS ,
AS IN A STACK YOU CAN ONLY GET ELEMENT ON TOP , SAME GOES 
WITH STACK DS TOO . IN ORDER TO ACESS LAST ELEMENT 
YOU NEED TO MOVE ALL EMEMENTS ON TOP . HENCE ITS A 
FILO DS ,
IN STACK BASICALLY TWO OPERATION IS PERFORMED 
PUSH = IT ADDS NEW ITEM TO TOP ,
POP = IT REMOVES TOP MOST  ITEM  
'''


class Stack:
    def __init__(self, lim=10, visual=False):
        self.visual = visual
        self.lim = lim
        self.stack = []

    def push(self, item):
        if not self.isfull():
            self.stack.append(item)
        else:
            print("STACK OVERFLOW")

        # visualisation
        if self.visual:
            print(f"pushed {item} ")
            self.visualize()

    def isfull(self):
        return len(self.stack) >= self.lim

    def isempty(self):
        return not bool(len(self.stack))

    def pop(self):
        if self.isempty() == False:
            item = self.stack.pop()
            if self.visual:
                print(f" popped {item}")
                self.visualize()
            return item
        return False

    def peek(self):
        return self.stack[-1]

    def visualize(self):
        for i in reversed(self.stack):
            print(f"[|||||||| {i} |||||||]")

    @staticmethod
    def testStack():
        S = Stack(10, True)

        for i in range(12):
            S.push(i)

        for i in range(12):
            S.pop()


if __name__ == '__main__':
    Stack.testStack()

