from ..Linear.SLL import SLL
from ..nodes.SNode import Node


class CSLL(SLL):
    def __init__(self, head=None):
        if head is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = head
            self.tail = head
            self.size = 1
            self.head.next = self.head

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head  # connect tail to head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head  # connect tail to head
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node  # set the next node to itself to close the loop
        else:
            self.tail.next = node
            self.tail = node
            node.next = self.head  # set the next node to the head to close the loop
        self.size += 1

    def Insert(self, node, position):
        if position < 1 or position > self.size + 1:
            print("Invalid position!")
            return
        if position == 1:
            if self.head is None:
                self.head = node
                self.tail = node
                node.next = node
            else:
                node.next = self.head
                self.head = node
                self.tail.next = node
        elif position == self.size + 1:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            current = self.head
            for i in range(1, position - 1):
                current = current.next
            node.next = current.next
            current.next = node
        self.size += 1

    def Search(self, node):
        curr_node = self.head
        while curr_node is not None and curr_node.next != self.head:
            if curr_node.data == node.data:
                return curr_node
            curr_node = curr_node.next
        if curr_node.data == node.data:
            return curr_node
        return None

    def SortedInsert(self, new_node):
        current = self.head
        if current is None:  # empty list
            self.InsertHead(new_node)
            return
        if current.data > new_node.data:  # new_node should be the new head
            self.InsertHead(new_node)
            return
        while current.next != self.head:
            if current.next.data > new_node.data:  # insert new_node here
                new_node.next = current.next
                current.next = new_node
                self.size += 1  # increment the size of the list
                return
            current = current.next
        # new_node should be the new tail
        self.InsertTail(new_node)

    def isSorted(self):
        if self.head is None or self.head.next is None:
            return True
        current = self.head
        while current and current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        if current.next.data < self.head.data:
            return False
        return True

    def DeleteHead(self):
        if self.head is None:
            return None
        elif self.head == self.tail:  # only one node in the list
            self.head = None
            self.tail = None
            self.size = 0
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head  # update tail's next to the new head
            temp.next = None
            self.size -= 1

    def DeleteTail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:  # if there's only one node in the list
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            # set the next node of the new tail to the head to close the loop
            current.next = self.head
            self.tail = current
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
                if current == self.head:  # if reached end of loop, set current to the last node in the list
                    current = self.tail
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
            while curr.next is not None and curr.next != self.head:
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
        return super().Clear()

    def Print(self):
        print(f"List size: {self.size}")
        if self.isSorted():
            print("Sorted: Yes")
        else:
            print("Sorted: No")
        current = self.head
        print("Contents of list are...\n")
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break
