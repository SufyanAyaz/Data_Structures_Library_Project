from ..nodes.SNode import Node


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __init__(self, head=None):
        if head is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = head
            self.tail = head
            self.size = 1

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def Insert(self, node, position):
        if position < 0:
            position = 0
        if position > self.size:
            position = self.size

        if self.head is None:
            self.head = node
            self.tail = node
        elif position == 0:
            node.next = self.head
            self.head = node
        elif position == self.size:
            self.tail.next = node
            self.tail = node
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node

        self.size += 1

    # Search for a node in the list
    def Search(self, node):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == node.data:
                return curr_node
            curr_node = curr_node.next
        return None

    def SortedInsert(self, node):
        if self.head is None:  # if list is empty
            self.InsertHead(node)
            return

        if not self.isSorted():  # if list is not sorted
            self.Sort()  # sort the list before inserting the node

        current = self.head
        previous = None

        while current is not None and current.data < node.data:
            previous = current
            current = current.next

        if previous is None:  # insert at head
            self.InsertHead(node)
        elif current is None:  # insert at tail
            self.InsertTail(node)
        else:  # insert at specific position
            self.Insert(node, self.getPosition(current.data) - 1)

    def getPosition(self, data):
        current = self.head
        position = 1

        while current is not None:
            if current.data == data:
                return position
            position += 1
            current = current.next

        return -1  # data not found in list

    def isSorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def DeleteHead(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.size -= 1

    def DeleteTail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
            self.tail.next = None
            self.size -= 1

    def Delete(self, node):
        if self.head == node:
            self.DeleteHead()
        elif self.tail == node:
            self.DeleteTail()
        else:
            current = self.head
            while current is not None and current.next != node:
                current = current.next
            if current is not None:
                temp = current.next
                current.next = temp.next
                temp.next = None
                self.size -= 1
        return None

    def Sort(self):
        if self.head is None or self.head.next is None:
            return

        swapped = True
        while swapped:
            swapped = False
            prev = None
            curr = self.head
            while curr.next is not None:
                if curr.data > curr.next.data:
                    if prev is not None:
                        prev.next = curr.next
                    else:
                        self.head = curr.next
                    temp = curr.next.next
                    curr.next.next = curr
                    curr.next = temp
                    prev = curr.next
                    swapped = True
                else:
                    prev = curr
                    curr = curr.next
        self.tail = curr

    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print(f"List size: {self.size}")
        if self.isSorted():
            print("Sorted: Yes")
        else:
            print("Sorted: No")
        current = self.head
        print("Contents of list are...\n")
        while current is not None:
            print(current.data)
            current = current.next
