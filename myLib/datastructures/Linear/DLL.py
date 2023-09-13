from ..nodes.DNode import DNode


class DLL:
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
            self.head.prev = node
            self.head = node
        node.prev = None
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        node.next = None
        self.size += 1

    def Insert(self, node, position):
        if position < 1 or position > self.size + 1:
            print("Invalid position!")
            return
        if position == 1:
            if self.head is None:  # if list is empty
                self.head = self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
        else:
            current = self.head
            current_position = 1
            while current_position < position - 1:
                current = current.next
                current_position += 1
            node.next = current.next
            node.prev = current
            if current.next is not None:
                current.next.prev = node
            current.next = node
            if node.next is None:
                self.tail = node
        self.size += 1

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
            node.prev = previous
            node.next = current
            current.prev = node
            previous.next = node
            self.size += 1

    def isSorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next

        current = self.tail
        while current and current.prev:
            if current.data < current.prev.data:
                return False
            current = current.prev

        return True

    def DeleteHead(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None  # update tail to None when last node is removed
            temp.next = None
            self.size -= 1

            # Update tail if there is only one node in the list
            if self.head is None and self.tail is not None:
                self.tail.prev = None

        return temp

    def DeleteTail(self):
        if self.tail is None:
            return None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            temp.prev = None
            self.size -= 1
            return temp

    def Delete(self, node):
        if self.head == node:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
        elif self.tail == node:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
        else:
            current = self.head
            while current is not None and current != node:
                current = current.next
            if current is not None:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                node.prev = None
                node.next = None
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
                    curr.next.prev = curr.prev  # set prev of curr.next to curr's prev
                    curr.prev = curr.next       # set curr's prev to curr.next
                    curr.next = temp
                    if temp is not None:
                        temp.prev = curr          # set prev of temp to curr
                    prev = curr.next
                    swapped = True
                else:
                    prev = curr
                    curr = curr.next
        self.tail = curr

    def Clear(self):
        current = self.head
        while current is not None:
            temp = current.next
            current.next = None
            current.prev = None
            current = temp
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
