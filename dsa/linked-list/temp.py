class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def pushBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pushLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    def insert(self, midNode, data):
        if midNode is None:
            print("middle node not present")
            return

        newNode = Node(data)
        newNode.next = midNode.next
        midNode.next = newNode

    def remove(self, key):
        headNode = self.head

        if headNode is not None:
            if headNode.data == key:
                self.head = headNode.next
                headNode = None
                return

            while headNode is not None:
                if headNode.data == key:
                    break
                prev = headNode
                headNode = headNode.next

            if headNode == None:
                return

            prev.next = headNode.next
            headNode = None

    def findMid(self):
        slow, fast = self.head, self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.pushBegin(100)
    ll.pushLast(500)

    ll.printList()

    temp = ll.head

    print(ll.findMid().data)

    # while temp != None:
    #     print(temp.data, end=" ")
    #     temp = temp.next
