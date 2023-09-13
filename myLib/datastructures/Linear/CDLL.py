from ..Linear.DLL import DLL
from ..nodes.DNode import DNode


class CDLL(DLL):
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
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size = 1

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = node
            node.next = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            node.prev = self.tail
            self.tail.next = node
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = node
            node.next = node
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
        self.size += 1

    def Insert(self, node, position):
        if position < 1 or position > self.size + 1:
            print("Invalid position!")
            return
        if position == 1:
            if self.head is None:  # empty list
                self.head = node
                self.tail = node
                node.prev = node  # self-referencing
                node.next = node  # self-referencing
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.head.prev = self.tail  # link head to tail
                self.tail.next = self.head  # link tail to head
        elif position == self.size + 1:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.head.prev = self.tail  # link head to tail
            self.tail.next = self.head  # link tail to head
        else:
            current = self.head
            for i in range(1, position - 1):
                current = current.next
            node.next = current.next
            current.next.prev = node
            current.next = node
            node.prev = current
        self.size += 1

    def Search(self, node):
        if self.head is None:
            return None
        curr_node = self.head
        while True:
            if curr_node.data == node.data:
                return curr_node
            curr_node = curr_node.next
            if curr_node is self.head:
                break
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
            if current == self.head:  # reached end of the list, insert at tail
                self.InsertTail(node)
                return

        if previous is None:  # insert at head
            self.InsertHead(node)
        elif current is None:  # insert at tail
            self.InsertTail(node)
        else:  # insert at specific position
            node.prev = previous
            node.next = current
            current.prev = node
            previous.next = node
            self.size += 1

    def isSorted(self):
        if self.head is None:
            return True

        current = self.head
        while current.next != self.head:
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
            if self.head is not None:
                self.head.prev = self.tail  # point the new head's prev to the tail
                self.tail.next = self.head  # point the tail's next to the new head
            else:
                self.tail = None
            temp.next = None
            temp.prev = None
            self.size -= 1
            return temp

    def DeleteTail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head  # close the loop
            self.head.prev = self.tail  # update prev attribute of head node
            self.size -= 1

    def Delete(self, node):
        if self.head == node:
            self.head = node.next
            if self.head == self.tail:  # if only one node in the list
                self.head.next = None
                self.tail.prev = None
                self.head.prev = None
                self.tail.next = None
                self.tail = self.head
            else:
                self.head.prev = None
                self.tail.next = self.head
            self.size -= 1
            return node

        current = self.head
        while current is not None and current != node:
            current = current.next

        if current is not None:
            if current == self.tail:
                self.tail = current.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

            current.next = None
            current.prev = None
            self.size -= 1
            return current

        return None

    def Sort(self):
        if self.head is None or self.head.next is None:
            return

        while True:
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
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next
                    curr.prev = curr.next
                    curr.next = temp
                    if temp is not None:
                        temp.prev = curr
                    prev = curr
                    swapped = True
                else:
                    prev = curr
                    curr = curr.next

            if not swapped:
                break

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
        while current is not None:
            print(current.data)
            current = current.next
            if current == self.head:  # reached end of list and looped back to head
                break
