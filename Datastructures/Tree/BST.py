'''
BINARY SEARCH TREE IMPLEMENTATION
BINARY SEARCH TREE IS A TREE BASED DATA STRUCTURE UN WHICH VALUE SMALLER
THAN PARENT NODE IS STORED TO ITS LEFT AND VALUE GREATER THAN PARENT NODE
IS STORED IN ITS RIGHT , BST NODE CAN HAVE MAXIMUM TWO CHILDS BUT 
MINIMUM CAN BE ZERO CHILD TOO
'''

# node class that defines building block
# for bst
# node has a key , name that can be a string its optional
# and two childs by default to none one left one right


class node:
    def __init__(self, key, name="no name yet"):
        self.key = key
        self.name = name
        self.left = None
        self.right = None


# bst class  by default root node is set to none
class BST:
    def __init__(self):
        self.root = None

    # method for in order traversal
    # gives visit nodes from smaller to greater
    def inorderTraversal(self, currentNode):
        # method takes start node
        # to start traversal currentNode

        if currentNode != None:
            # if current node is not none
            # call inorderTraversal to its left child
            # print currentNodes key
            # call inorderTraversal to its right child
            self.inorderTraversal(currentNode.left)
            print(currentNode.key)
            self.inorderTraversal(currentNode.right)

    # similar to inorder traversal
    # just we print key before calling method recursiveliy
    # to both of its child
    def preorderTraversal(self, currentNode):

        if currentNode != None:
            print(currentNode.key)
            self.preorderTraversal(currentNode.left)
            self.preorderTraversal(currentNode.right)

    # similar to in order traversal just
    # we print key at last after calling
    # method recursively to both of its child
    def postorderTraversal(self, currentNode):

        if currentNode != None:

            self.postorderTraversal(currentNode.left)
            self.postorderTraversal(currentNode.right)
            print(currentNode.key)

    # method to add node

    def addNodes(self, key):
        # create new node using key passed
        n = node(key)

    # if root is none which means tree is empty
    # set n as root

        if self.root == None:
            self.root = n

    # else traverse tree to find appropriate position for
    # node
        else:
            # at start currentNode = root
            currentNode = self.root

    # while current node is true
            while currentNode:
                # set parent to current node
                parent = currentNode

        # and if key of node to be added is smaller
        # than current node
        # set currentnode to its left child
        # if current node is none
        # set parents left to newnode
        # and return

                if key < currentNode.key:

                    currentNode = currentNode.left

                    if currentNode == None:
                        parent.left = n
                        return
                # and if key of node to be added is greater
        # than current node
        # set currentnode to its right child
        # if current node is none
        # set parents right to newnode
        # and return
                else:
                    currentNode = currentNode.right
                    if currentNode == None:
                        parent.right = n
                        return

    def remove(self, key):
        currentNode = self.root
        parent = self.root
        isAtLeft = True

        # Finding Phase

        while currentNode.key != key:

            parent = currentNode

            if key < currentNode.key:
                isAtLeft = True
                currentNode = currentNode.left

            else:
                isAtLeft = False
                currentNode = currentNode.right

            # If its not found

            if currentNode == None:
                return False

        # Removing Phase behind
        # If item to be removed found
        # and have no children
        # ( Leaf Format )
        if currentNode.left == None and currentNode.right == None:

            # if its root node
            if currentNode == self.root:
                # delete root
                self.root = None

            # if found node is not root
            # and its a left child

            elif isAtLeft:
                # delete found node
                parent.left = None
            else:
                # if its not a left child
                # its a right child
                # delete the node
                parent.right = None

        # if found node has a left child
        # but no right child
        elif currentNode.right == None:

            # if it's root nose
            if currentNode == self.root:
                # delete it and replace
                # it with its left child
                self.root = currentNode.left

            # else if it's a left child
            elif isAtLeft:
                parent.left = currentNode.left

            # else it's a right child
            else:
                parent.right = currentNode.left

        # else if it has a right child
        # but no left child
        elif currentNode.left == None:

            # if it's root nose
            if currentNode == self.root:
                # delete it and replace
                # it with its left child
                self.root = currentNode.right

            # else if it's a left child
            elif isAtLeft:
                parent.right = currentNode.right

            # else it's a right child
            else:
                parent.right = currentNode.left

        # else have both left and right child
        else:
            replacement = self.getReplacement(currentNode)

            # if it's root
            if currentNode == self.root:
                self.root = replacement
            # if it's a left child
            elif isAtLeft:
                parent.left = replacement
            else:
                parent.right = replacement

            # finally set replacements
            # left child
            # to current left child
            replacement.left = currentNode.left

        return True

    def getReplacement(self, toReplace):

        replacementParent = toReplace
        replacement = toReplace

        cur = toReplace.right

        while cur != None:
            replacementParent = replacement
            replacement = cur
            cur = cur.left

        if replacement != toReplace.right:
            replacementParent.left = replacement.right

            replacement.right = toReplace.right

        return replacement


bst = BST()
bst.addNodes(1)
bst.addNodes(5)
bst.addNodes(3)
bst.addNodes(7)


bst.remove(5)

bst.addNodes(10)
bst.addNodes(4)
bst.inorderTraversal(bst.root)


print()
print()
bst.preorderTraversal(bst.root)

print()
print()
bst.postorderTraversal(bst.root)
