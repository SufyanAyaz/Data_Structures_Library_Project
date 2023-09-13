from ..Linear.SLL import SLL
from ..nodes.SNode import Node


class QueueLL(SLL):
    def __init__(self):
        super().__init__()

    def __init__(self, head=None):
        super().__init__(head)

    def InsertHead(self, node):
        return

    def Enqueue(self, node):
        super().InsertTail(node)

    def Insert(self, node, position):
        return

    def Search(self, node):
        curr_node = self.head
        position = 1
        while curr_node is not None:
            if curr_node.data == node.data:
                return position
            curr_node = curr_node.next
            position += 1
        return None

    def SortedInsert(self, node):
        return

    def Dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            if self.head is None:  # if there are no nodes left in the list
                self.tail = None
            self.size -= 1
            return temp

    def DeleteTail(self):
        return

    def Delete(self, node):
        return

    def Sort(self):
        return

    def Clear(self):
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            current = next_node
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print(f"Queue size: {self.size}")
        current = self.head
        print("Contents of queue are...")
        while current is not None:
            print(current.data)
            current = current.next
