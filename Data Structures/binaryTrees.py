class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def display(self):
        print(self.data)

class BinaryTree:
    def __init__(self):
        self.rootNode = None

    def insert(self, value):
        if self.rootNode is None:
            newNode = Node(value)
            self.rootNode = newNode
        else:
            self.recursiveInsert(self.rootNode, value)

    def remove(self, value):
        if self.rootNode:
            self.recursiveRemove(self.rootNode, value)
        else:
            print("Nothing there D:")

    def recursiveRemove(self, currentNode, value):
        if currentNode is None:
            return None

        else:
            if value < currentNode.data:
                currentNode.leftChild = self.recursiveRemove(currentNode.leftChild, value)

            elif value > currentNode.data:
                currentNode.rightChild = self.recursiveRemove(currentNode.rightChild, value)

            else:
                # 1. Node has no child
                if currentNode.rightChild is None and currentNode.leftChild is None:
                    return None

                # 2. Node has 1 child

                if currentNode.rightChild is None:
                    return currentNode.leftChild

                elif currentNode.leftChild is None:
                    return currentNode.rightChild

                #3. Node has 2 children

                if currentNode.rightChild and currentNode.leftChild:
                    None #----> Work in progress


    def recursiveInsert(self, currentNode, value): # :D
        if value > currentNode.data:
            if currentNode.rightChild is None:
                currentNode.rightChild = Node(value)

            else:
                self.recursiveInsert(currentNode.rightChild, value)

        else:
            if currentNode.leftChild is None:
                currentNode.leftChild = Node(value)

            else:
                self.recursiveInsert(currentNode.leftChild, value)

    def inorderTraversal(self, currentNode):
        if currentNode:
            self.inorderTraversal(currentNode.leftChild)
            print(currentNode.data, end = " ")
            self.inorderTraversal(currentNode.rightChild)

    def preOrderTraversal(self, currentNode):
        if currentNode:
            print(currentNode.data, end = " ")
            self.inorderTraversal(currentNode.leftChild)
            self.inorderTraversal(currentNode.rightChild)

    def postOrderTraversal(self, currentNode):
        if currentNode:
            self.inorderTraversal(currentNode.leftChild)
            self.inorderTraversal(currentNode.rightChild)
            print(currentNode.data, end = " ")

object1 = BinaryTree()
object1.insert(50)
object1.insert(21)
object1.insert(17)
object1.insert(91)
object1.insert(62)
object1.insert(50)
object1.inorderTraversal(object1.rootNode)
print()
object1.postOrderTraversal(object1.rootNode)
print()
object1.preOrderTraversal(object1.rootNode)
