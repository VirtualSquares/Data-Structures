class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def removeNodeFromHead(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("empty")

    def insertAtIndex(self, data, placementIndex):
        newNode = Node(data)
        currentIndex = 0
        currentNode = self.head

        while currentIndex < placementIndex - 1 and currentNode:
            currentIndex += 1
            currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode

    def removeNodeAtIndex(self, index):
        if self.head is None:
            print("empty")
            return

        if index == 0:
            self.head = self.head.next
            return

        currentNode = self.head
        currentIndex = 0

        while currentNode is not None and currentIndex < index - 1:
            currentNode = currentNode.next
            currentIndex += 1

        if currentNode is None or currentNode.next is None:
            print("error")
            return

        currentNode.next = currentNode.next.next

    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

linkedList = LinkedList()

linkedList.insertNodeAtHead(3)
linkedList.insertNodeAtHead(4)
linkedList.insertNodeAtHead(5)

linkedList.insertAtIndex(10, 2)
linkedList.insertAtIndex(50, 4)

linkedList.display()

linkedList.removeNodeAtIndex(2)

linkedList.display()

linkedList.removeNodeAtIndex(10)
