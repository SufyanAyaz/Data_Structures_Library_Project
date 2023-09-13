import pytest
from myLib.datastructures.Linear.CDLL import CDLL
from myLib.datastructures.nodes.DNode import DNode

# Test the initialization of the CDLL class with no arguments


def test_cdll_init_no_args():
    cdll = CDLL()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0

# Test the initialization of the CDLL class with a single node


def test_cdll_init_one_node():
    node = DNode(1)
    cdll = CDLL(node)
    assert cdll.head == node
    assert cdll.tail == node
    assert cdll.size == 1

# Test the InsertHead function


def test_cdll_insert_head():
    cdll = CDLL()
    node1 = DNode(1)
    cdll.InsertHead(node1)
    assert cdll.head == node1
    assert cdll.tail == node1
    assert cdll.size == 1
    node2 = DNode(2)
    cdll.InsertHead(node2)
    assert cdll.head == node2
    assert cdll.tail == node1
    assert cdll.size == 2

# Test the InsertTail function


def test_cdll_insert_tail():
    cdll = CDLL()
    node1 = DNode(1)
    cdll.InsertTail(node1)
    assert cdll.head == node1
    assert cdll.tail == node1
    assert cdll.size == 1
    node2 = DNode(2)
    cdll.InsertTail(node2)
    assert cdll.head == node1
    assert cdll.tail == node2
    assert cdll.size == 2

# Test the Insert function


def test_cdll_insert():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    cdll.Insert(node1, 1)
    assert cdll.head == node1
    assert cdll.tail == node1
    assert cdll.size == 1
    cdll.Insert(node2, 2)
    assert cdll.head == node1
    assert cdll.tail == node2
    assert cdll.size == 2
    cdll.Insert(node3, 2)
    assert cdll.head == node1
    assert cdll.tail == node2
    assert cdll.size == 3

# Test the Search function


def test_cdll_search():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    cdll.InsertTail(node1)
    cdll.InsertTail(node2)
    cdll.InsertTail(node3)
    assert cdll.Search(node2) == node2
    assert cdll.Search(DNode(4)) == None


def test_SortedInsert_empty():
    cdll = CDLL()
    node = DNode(1)
    cdll.SortedInsert(node)
    assert cdll.head == node
    assert cdll.tail == node


def test_SortedInsert_unsorted():
    cdll = CDLL()
    cdll.InsertTail(DNode(1))
    cdll.InsertTail(DNode(3))
    cdll.SortedInsert(DNode(2))
    assert cdll.isSorted() == True
    assert cdll.size == 3


def test_SortedInsert_sorted():
    cdll = CDLL()
    cdll.InsertTail(DNode(1))
    cdll.InsertTail(DNode(2))
    cdll.InsertTail(DNode(3))
    cdll.SortedInsert(DNode(4))
    assert cdll.isSorted() == True
    assert cdll.size == 4


def test_DeleteHead():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    cdll.InsertTail(node1)
    cdll.InsertTail(node2)
    cdll.InsertTail(node3)
    assert cdll.head == node1
    assert cdll.DeleteHead() == node1
    assert cdll.head == node2
    assert cdll.size == 2


def test_DeleteTail():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    cdll.InsertTail(node1)
    cdll.InsertTail(node2)
    cdll.InsertTail(node3)

    cdll.DeleteTail()
    assert cdll.tail == node2
    assert cdll.tail.next == node1
    assert node1.prev == node2


def test_Delete():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    cdll.InsertTail(node1)
    cdll.InsertTail(node2)
    cdll.InsertTail(node3)
    assert cdll.Delete(node2) == node2
    assert cdll.size == 2


def test_Sort():
    cdll = CDLL()
    cdll.InsertTail(DNode(3))
    cdll.InsertTail(DNode(2))
    cdll.InsertTail(DNode(1))
    cdll.Sort()
    assert cdll.isSorted() == True
    assert cdll.size == 3


def test_Clear():
    cdll = CDLL()
    cdll.InsertTail(DNode(1))
    cdll.InsertTail(DNode(2))
    cdll.Clear()
    assert cdll.head == None
    assert cdll.tail == None
    assert cdll.size == 0


def test_Print(capsys):
    cdll = CDLL()
    cdll.InsertTail(DNode(1))
    cdll.InsertTail(DNode(2))
    cdll.InsertTail(DNode(3))
    cdll.Print()
    out, err = capsys.readouterr()
    assert out == "List size: 3\nSorted: Yes\nContents of list are...\n\n1\n2\n3\n"
