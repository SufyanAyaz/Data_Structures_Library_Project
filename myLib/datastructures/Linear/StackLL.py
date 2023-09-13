from ..Linear.SLL import SLL
from ..nodes.SNode import Node


class StackLL(SLL):
    def __init__(self):
        super().__init__()

    def __init__(self, head=None):
        super().__init__(head)

    def Push(self, node):
        super().InsertHead(node)

    def InsertTail(self, node):
        return

    def Insert(self, node, index):
        return

    def Search(self, node):
        curr_node = self.head
        index = self.size
        while curr_node is not None:
            if curr_node.data == node.data:
                return index
            curr_node = curr_node.next
            index -= 1
        return -1

    def SortedInsert(self, node):
        return

    def isSorted(self):
        if self.head is None:
            return True
        curr = self.head
        prev_data = curr.data
        while curr.next:
            if curr.next.data > prev_data:
                return False
            prev_data = curr.next.data
            curr = curr.next
        return True

    def Pop(self):
        temp = self.head
        super().DeleteHead()
        return temp

    def DeleteTail(self):
        return

    def Delete(self, node):
        return

    def Sort(self):
        return

    def Clear(self):
        while self.head is not None:
            self.Pop()
        self.size = 0

    def Print(self):
        print(f"Stack size: {self.size}")
        current = self.head
        print("Contents of stack are...\n")
        while current is not None:
            print(current.data)
            current = current.next
