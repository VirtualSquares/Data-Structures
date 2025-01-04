class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtHead(self, data):
        newNode = Node(data)
        if self.head:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

        else:
            self.head = newNode
            self.tail = newNode

    def InsertAtTail(self, data):
        newNode = Node(data)
        if self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        else:
            self.head = newNode
            self.tail = newNode

    def InsertAtIndex(self, data, pos):
        newNode = Node(data)
        if pos == 0:
            self.InsertAtHead(data)

        else:
            currentNode = self.head
            currentIndex = 0

            while currentNode:
                if currentIndex == pos:
                    newNode.next = currentNode
                    newNode.prev = currentNode.prev
                    currentNode.prev.next = newNode
                    currentNode.prev = newNode

                currentIndex += 1
                currentNode = currentNode.next

    def RemoveAtHead(self):
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None

        elif self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            print("List Empty")

    def RemoveAtTail(self):
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None

        elif self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            print("List Empty")

    def RemoveAtIndex(self, index):
        if self.head == None:
            print("Empty List")
            return

        if index == 0:
            self.RemoveAtHead()

        elif index < 0:
            print("Invalid Index")
            return

        else:
            currentNode, cnt = self.head, 0
            while currentNode:
                if cnt == index:

                    if currentNode.next == None:
                        self.RemoveAtTail()

                    else:
                        currentNode.prev.next = currentNode.next
                        currentNode.next.prev = currentNode.prev
                        currentNode.next, currentNode.prev = None, None
                currentNode = currentNode.next
                cnt += 1

    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end = " ")
            currentNode = currentNode.next

        print()


linkedList = DoublyLinkedList()

linkedList.InsertAtHead(3)
linkedList.InsertAtHead(4)
linkedList.InsertAtHead(5)

linkedList.InsertAtIndex(10, 2)
linkedList.InsertAtIndex(50, 4)

linkedList.display()

linkedList.RemoveAtIndex(2)

linkedList.display()

linkedList.RemoveAtIndex(1)
linkedList.display()





