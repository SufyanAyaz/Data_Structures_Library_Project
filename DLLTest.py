import pytest
from myLib.datastructures.Linear.DLL import DLL
from myLib.datastructures.nodes.DNode import DNode


def test_DLL_init_with_no_arguments():
    doubly_ll = DLL()
    assert doubly_ll.head is None
    assert doubly_ll.tail is None
    assert doubly_ll.size == 0


def test_DLL_init_with_head_node():
    node = DNode(10)
    doubly_ll = DLL(node)
    assert doubly_ll.head is node
    assert doubly_ll.tail is node
    assert doubly_ll.size == 1


def test_InsertHead():
    dll = DLL()
    dll.InsertHead(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    dll.InsertHead(DNode(2))
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.head.next.data == 1
    assert dll.tail.prev.data == 2
    assert dll.size == 2


def test_InsertTail():
    dll = DLL()
    dll.InsertTail(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    dll.InsertTail(DNode(2))
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.head.next.data == 2
    assert dll.tail.prev.data == 1
    assert dll.size == 2


def test_Insert():
    dll = DLL()
    dll.Insert(DNode(1), 1)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    dll.Insert(DNode(2), 2)
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.head.next.data == 2
    assert dll.tail.prev.data == 1
    assert dll.size == 2

    dll.Insert(DNode(3), 2)
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.head.next.data == 3
    assert dll.tail.prev.data == 3
    assert dll.head.next.next.data == 2
    assert dll.tail.prev.prev.data == 1
    assert dll.size == 3


def test_Search():
    dll = DLL()
    dll.InsertTail(DNode(1))
    dll.InsertTail(DNode(2))
    dll.InsertTail(DNode(3))
    node = dll.Search(DNode(2))
    assert node.data == 2

    node = dll.Search(DNode(4))
    assert node == None


def test_SortedInsert():
    dll = DLL()
    dll.SortedInsert(DNode(2))
    dll.SortedInsert(DNode(1))
    dll.SortedInsert(DNode(3))
    assert dll.head.data == 1
    assert dll.tail.data == 3
    assert dll.head.next.data == 2
    assert dll.head.next.next.data == 3
    assert dll.tail.prev.data == 2
    assert dll.tail.prev.prev.data == 1
    assert dll.size == 3


def test_isSorted():
    dll = DLL()
    assert dll.isSorted() == True

    dll = DLL(DNode(1))
    assert dll.isSorted() == True

    dll = DLL(DNode(1))
    dll.head.next = DNode(2)
    dll.head.next.prev = dll.head
    dll.size = 2
    assert dll.isSorted() == True

    dll = DLL(DNode(2))
    dll.head.next = DNode(1)
    dll.head.next.prev = dll.head
    dll.size = 2
    assert dll.isSorted() == False


def test_DeleteHead():
    # Test deleting head from an empty list
    dll = DLL()
    assert dll.DeleteHead() is None

    # Test deleting head from a list with one node
    dll = DLL(DNode(1))
    assert dll.DeleteHead().data == 1
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0

    # Test deleting head from a list with two nodes
    dll = DLL(DNode(1))
    dll.head.next = DNode(2)
    dll.head.next.prev = dll.head
    dll.tail = dll.head.next
    dll.size = 2
    assert dll.DeleteHead().data == 1
    assert dll.head.data == 2
    assert dll.head.prev is None
    assert dll.tail.prev is None
    assert dll.tail.data == 2

    # Test deleting head from a list with more than two nodes
    dll = DLL(DNode(1))
    dll.head.next = DNode(2)
    dll.head.next.prev = dll.head
    dll.head.next.next = DNode(3)
    dll.head.next.next.prev = dll.head.next
    dll.tail = dll.head.next.next
    dll.size = 3
    assert dll.DeleteHead().data == 1
    assert dll.head.data == 2
    assert dll.head.prev is None
    assert dll.tail.prev is dll.head

    # Test deleting head from a list with only one node and updating tail
    dll = DLL(DNode(1))
    dll.tail = dll.head
    assert dll.DeleteHead().data == 1
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0

    # Test deleting head from a list with two nodes and updating tail
    dll = DLL(DNode(1))
    dll.head.next = DNode(2)
    dll.head.next.prev = dll.head
    dll.tail = dll.head.next
    dll.size = 2
    assert dll.DeleteHead().data == 1
    assert dll.head.data == 2
    assert dll.head.prev is None
    assert dll.tail.prev is None
    assert dll.tail is dll.head


def test_DeleteTail():
    dll = DLL()
    assert dll.DeleteTail() == None

    dll = DLL(DNode(1))
    assert dll.DeleteTail().data == 1
    assert dll.head == None
    assert dll.tail == None
    assert dll.size == 0

    dll = DLL(DNode(1))
    dll.head.next = DNode(2)
    dll.head.next.prev = dll.head
    dll.tail = dll.head.next
    dll.size = 2
    assert dll.DeleteTail().data == 2
    assert dll.tail == dll.head
    assert dll.tail.next == None
    assert dll.head.next == None
    assert dll.size == 1


def test_delete():
    dll = DLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    dll.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    dll.tail = node3
    dll.size = 3

    dll.Delete(node1)
    assert dll.head == node2
    assert dll.tail == node3
    assert node2.prev is None
    assert node2.next == node3
    assert node3.prev == node2

    dll.Delete(node3)
    assert dll.head == node2
    assert dll.tail == node2
    assert node2.prev is None
    assert node2.next is None


def test_sort():
    dll = DLL()
    node1 = DNode(1)
    node2 = DNode(4)
    node3 = DNode(2)
    dll.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    dll.tail = node3
    dll.size = 3

    dll.Sort()

    assert dll.head == node1
    assert dll.tail == node2
    assert node1.prev is None
    assert node1.next == node3
    assert node2.prev == node3
    assert node2.next is None
    assert node3.prev == node1
    assert node3.next == node2


def test_clear():
    dll = DLL()
    node1 = DNode(1)
    node2 = DNode(2)
    dll.head = node1
    node1.next = node2
    node2.prev = node1
    dll.tail = node2
    dll.size = 2

    dll.Clear()

    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0


def test_print(capsys):
    dll = DLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    dll.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    dll.tail = node3
    dll.size = 3

    dll.Sort()
    dll.Print()

    captured = capsys.readouterr()
    expected_output = "List size: 3\nSorted: Yes\nContents of list are...\n\n1\n2\n3\n"
    assert captured.out == expected_output
