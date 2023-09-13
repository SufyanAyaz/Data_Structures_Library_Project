import pytest
from myLib.datastructures.Linear.CSLL import CSLL
from myLib.datastructures.nodes.SNode import Node


def test_CSLL_init():
    linked_list = CSLL()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0

    node = Node(5)
    linked_list = CSLL(node)
    assert linked_list.head == node
    assert linked_list.tail == node
    assert linked_list.size == 1


def test_InsertHead():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list = CSLL()
    linked_list.InsertHead(node1)
    assert linked_list.head == node1
    assert linked_list.tail == node1
    assert linked_list.size == 1
    linked_list.InsertHead(node2)
    assert linked_list.head == node2
    assert linked_list.tail == node1
    assert linked_list.size == 2
    linked_list.InsertHead(node3)
    assert linked_list.head == node3
    assert linked_list.tail == node1
    assert linked_list.size == 3


def test_InsertTail():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list = CSLL()
    linked_list.InsertTail(node1)
    assert linked_list.head == node1
    assert linked_list.tail == node1
    assert linked_list.size == 1
    linked_list.InsertTail(node2)
    assert linked_list.head == node1
    assert linked_list.tail == node2
    assert linked_list.size == 2
    linked_list.InsertTail(node3)
    assert linked_list.head == node1
    assert linked_list.tail == node3
    assert linked_list.size == 3


def test_Insert():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list = CSLL()
    linked_list.Insert(node1, 1)
    assert linked_list.head == node1
    assert linked_list.tail == node1
    assert linked_list.size == 1
    linked_list.Insert(node2, 1)
    assert linked_list.head == node2
    assert linked_list.tail == node1
    assert linked_list.size == 2
    linked_list.Insert(node3, 3)
    assert linked_list.head == node2
    assert linked_list.tail == node3
    assert linked_list.size == 3


def test_Search():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list = CSLL(node1)
    linked_list.InsertTail(node2)
    linked_list.InsertTail(node3)
    assert linked_list.Search(node1) == node1
    assert linked_list.Search(node2) == node2
    assert linked_list.Search(node3) == node3
    assert linked_list.Search(Node(4)) == None


def test_SortedInsert():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    linked_list = CSLL(node1)
    linked_list.InsertTail(node3)
    linked_list.InsertTail(node4)
    linked_list.SortedInsert(node5)
    assert linked_list.head == node1
    assert linked_list.tail == node5
    assert linked_list.size == 4
    linked_list.SortedInsert(node2)
    assert linked_list.head == node1
    assert linked_list.tail == node5
    assert linked_list.size == 5
    assert linked_list.Search(node2).next == node3
    assert linked_list.Search(node5).next == node1


def test_is_sorted():
    # test with empty list
    csll = CSLL()
    assert csll.isSorted() == True

    # test with one node
    node1 = Node(1)
    csll = CSLL(node1)
    assert csll.isSorted() == True

    # test with two nodes
    node2 = Node(2)
    csll = CSLL(node1)
    csll.SortedInsert(node2)
    assert csll.isSorted() == True

    # test with multiple nodes
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    csll = CSLL(node1)
    csll.SortedInsert(node2)
    csll.SortedInsert(node3)
    csll.SortedInsert(node4)
    csll.SortedInsert(node5)
    assert csll.isSorted() == True

    # test with multiple nodes unsorted
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    csll = CSLL(node5)
    csll.InsertHead(node2)
    csll.InsertTail(node3)
    csll.InsertHead(node4)
    csll.InsertTail(node1)
    assert csll.isSorted() == False


def test_delete_head():
    # test with empty list
    csll = CSLL()
    assert csll.DeleteHead() == None

    # test with one node
    node1 = Node(1)
    csll = CSLL(node1)
    csll.DeleteHead()
    assert csll.head == None
    assert csll.tail == None
    assert csll.size == 0

    # test with multiple nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    csll = CSLL(node1)
    csll.SortedInsert(node2)
    csll.SortedInsert(node3)
    csll.SortedInsert(node4)
    csll.DeleteHead()
    assert csll.head.data == 2
    assert csll.tail.data == 4
    assert csll.size == 3


def test_DeleteTail():
    # Test for empty list
    lst = CSLL()
    assert lst.DeleteTail() == None

    # Test for list with single node
    lst = CSLL(Node(1))
    lst.DeleteTail()
    assert lst.head == None
    assert lst.tail == None
    assert lst.size == 0

    # Test for list with multiple nodes
    lst = CSLL(Node(1))
    lst.head.next = Node(2)
    lst.head.next.next = Node(3)
    lst.tail = lst.head.next.next
    lst.size = 3
    lst.DeleteTail()
    assert lst.tail.data == 2
    assert lst.head.next.next == lst.head
    assert lst.size == 2


def test_Delete():
    # Test for empty list
    lst = CSLL()
    assert lst.Delete(Node(1)) == None

    # Test for deleting head node
    lst = CSLL(Node(1))
    lst.head.next = Node(2)
    lst.tail = lst.head.next
    lst.size = 2
    lst.Delete(lst.head)
    assert lst.head.data == 2
    assert lst.tail.next == lst.head
    assert lst.size == 1

    # Test for deleting tail node
    lst = CSLL(Node(1))
    lst.head.next = Node(2)
    lst.tail = lst.head.next
    lst.size = 2
    lst.Delete(lst.tail)
    assert lst.head.data == 1
    assert lst.tail.next == lst.head
    assert lst.size == 1

    # Test for deleting middle node
    lst = CSLL(Node(1))
    lst.head.next = Node(2)
    lst.head.next.next = Node(3)
    lst.head.next.next.next = Node(4)
    lst.tail = lst.head.next.next.next
    lst.size = 4
    lst.Delete(lst.head.next)
    assert lst.head.next.data == 3
    assert lst.head.next.next == lst.tail
    assert lst.size == 3


def test_Sort():
    # Test for empty list
    lst = CSLL()
    lst.Sort()
    assert lst.head == None
    assert lst.tail == None
    assert lst.size == 0

    # Test for list with single node
    lst = CSLL(Node(1))
    lst.Sort()
    assert lst.head.data == 1
    assert lst.tail.data == 1
    assert lst.size == 1

    # Test for list with multiple nodes
    lst = CSLL(Node(2))
    lst.head.next = Node(3)
    lst.head.next.next = Node(1)
    lst.tail = lst.head.next.next
    lst.size = 3
    lst.Sort()
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.tail.data == 3
    assert lst.head.next.next == lst.tail
    assert lst.size == 3


def test_Clear():
    lst = CSLL(Node(1))
    lst.head.next = Node(2)
    lst.tail = lst.head.next
    lst.size = 2
    lst.Clear()
    assert lst.head == None
    assert lst.tail == None
    assert lst.size == 0


def test_CSLL_Print(capsys):
    linked_list = CSLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list.InsertHead(node1)
    linked_list.InsertHead(node2)
    linked_list.InsertHead(node3)

    linked_list.Print()
    captured = capsys.readouterr()
    expected_output = "List size: 3\nSorted: No\nContents of list are...\n\n3\n2\n1\n"
    assert captured.out == expected_output
