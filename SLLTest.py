import pytest
from myLib.datastructures.Linear.SLL import SLL
from myLib.datastructures.nodes.SNode import Node


def test_singly_linked_list_default_constructor():
    sll = SLL()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0


def test_singly_linked_list_overloaded_constructor():
    node = Node(1)
    sll = SLL(node)
    assert sll.head == node
    assert sll.tail == node
    assert sll.size == 1


def test_insert_head():
    sll = SLL()
    node1 = Node(1)
    node2 = Node(2)
    sll.InsertHead(node1)
    assert sll.head == node1 and sll.tail == node1 and sll.size == 1
    sll.InsertHead(node2)
    assert sll.head == node2 and sll.tail == node1 and sll.size == 2


def test_insert_tail():
    sll = SLL()
    node1 = Node(1)
    node2 = Node(2)
    sll.InsertTail(node1)
    assert sll.head == node1 and sll.tail == node1 and sll.size == 1
    sll.InsertTail(node2)
    assert sll.head == node1 and sll.tail == node2 and sll.size == 2


def test_insert():
    sll = SLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    sll.Insert(node1, 0)
    assert sll.head == node1 and sll.tail == node1 and sll.size == 1
    sll.Insert(node2, 1)
    assert sll.head == node1 and sll.tail == node2 and sll.size == 2
    sll.Insert(node3, 1)
    assert sll.head == node1 and sll.tail == node2 and sll.size == 3
    sll.Insert(node4, 3)
    assert sll.head == node1 and sll.tail == node4 and sll.size == 4


def test_search():
    sll = SLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    sll.InsertHead(node1)
    sll.InsertTail(node2)
    sll.Insert(node3, 1)
    assert sll.Search(node1) == node1
    assert sll.Search(node2) == node2
    assert sll.Search(node3) == node3
    assert sll.Search(Node(4)) is None


def test_sorted_insert():
    sll = SLL()
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(25)
    sll.InsertHead(node1)
    sll.InsertTail(node3)
    sll.Insert(node2, 1)
    sll.SortedInsert(node4)
    assert sll.head.data == 10
    assert sll.head.next.data == 20
    assert sll.head.next.next.data == 25
    assert sll.head.next.next.next.data == 30
    assert sll.size == 4


def test_delete_head():
    sll = SLL()
    node1 = Node(10)
    node2 = Node(20)
    sll.InsertHead(node1)
    sll.InsertTail(node2)
    sll.DeleteHead()
    assert sll.head.data == 20
    assert sll.tail.data == 20
    assert sll.size == 1


def test_DeleteTail():
    sll = SLL()
    sll.InsertHead(Node(1))
    sll.InsertHead(Node(2))
    sll.InsertHead(Node(3))
    sll.DeleteTail()
    assert sll.size == 2
    assert sll.tail.data == 2


def test_Delete():
    ll = SLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.InsertHead(node1)
    ll.InsertTail(node2)
    ll.InsertTail(node3)
    ll.Delete(node2)
    assert ll.head == node1
    assert ll.tail == node3
    assert ll.size == 2


def test_Sort():
    ll = SLL()
    node1 = Node(3)
    node2 = Node(1)
    node3 = Node(2)
    ll.InsertHead(node1)
    ll.InsertHead(node2)
    ll.InsertHead(node3)
    ll.Sort()
    assert ll.head == node2
    assert ll.tail == node1


def test_Clear():
    ll = SLL()
    node1 = Node(1)
    node2 = Node(2)
    ll.InsertHead(node1)
    ll.InsertTail(node2)
    ll.Clear()
    assert ll.head == None
    assert ll.tail == None
    assert ll.size == 0


def test_Print(capsys):
    sll = SLL()
    sll.InsertHead(Node(1))
    sll.InsertHead(Node(2))
    sll.InsertHead(Node(3))
    sll.Print()
    captured = capsys.readouterr()
    assert captured.out == "List size: 3\nSorted: No\nContents of list are...\n\n3\n2\n1\n"


# if __name__ == "__main__":
#     print("TESTING SLL \n")
#     test_singly_linked_list_default_constructor()
#     test_singly_linked_list_overloaded_constructor()
#     test_insert_head()
#     test_insert_tail()
#     test_insert()
#     test_search()
#     test_sorted_insert()
#     test_delete_head()
#     test_DeleteTail()
#     test_Delete()
#     test_Sort()
#     test_Clear()
#     test_Print()
