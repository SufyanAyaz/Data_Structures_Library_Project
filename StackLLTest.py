import pytest
from myLib.datastructures.Linear.StackLL import StackLL
from myLib.datastructures.nodes.SNode import Node


def test_init_default():
    stack = StackLL()
    assert stack.head is None
    assert stack.tail is None
    assert stack.size == 0


def test_init_with_head():
    node = Node(1)
    stack = StackLL(head=node)
    assert stack.head == node
    assert stack.tail == node
    assert stack.size == 1


def test_Push():
    # setup
    stack = StackLL()
    node = Node(1)

    # execute
    stack.Push(node)

    # assert
    assert stack.head == node
    assert stack.size == 1


def test_InsertTail():
    # setup
    stack = StackLL()
    node = Node(1)

    # execute
    stack.Push(node)

    # assert
    assert stack.head == node
    assert stack.tail == node
    assert stack.size == 1


def test_Insert():
    # setup
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    stack.Push(node1)
    stack.Push(node3)

    # execute
    temp = stack.Pop()
    stack.Push(node2)
    stack.Push(temp)

    # assert
    assert stack.Pop() == node3
    assert stack.Pop() == node2
    assert stack.Pop() == node1
    assert stack.size == 0


def test_Search():
    # setup
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    stack.Push(node1)
    stack.Push(node2)
    stack.Push(node3)

    # execute
    result1 = stack.Search(node2)
    result2 = stack.Search(Node(4))

    # assert
    assert result1 == 2
    assert result2 == -1


def test_SortedInsert():
    # setup
    stack = StackLL()

    # execute
    node1 = Node(1)
    stack.SortedInsert(node1)
    node2 = Node(2)
    stack.SortedInsert(node2)
    node3 = Node(3)
    stack.SortedInsert(node3)
    node4 = Node(4)
    stack.SortedInsert(node4)

    # assert
    if stack.size > 0:
        assert stack.head == node4
        assert stack.head.next.data == 3
        assert stack.head.next.next.data == 2
        assert stack.head.next.next.next.data == 1
    else:
        assert stack.head is None


def test_isSorted():
    # setup
    stack1 = StackLL()
    stack2 = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    stack1.Push(node1)
    stack1.Push(node2)
    stack1.Push(node3)
    stack1.Push(node4)
    stack2.Push(node1)
    stack2.Push(node3)
    stack2.Push(node2)

    # execute
    result1 = stack1.isSorted()
    result2 = stack2.isSorted()

    # assert
    assert result1 == True
    assert result2 == False


def test_Pop():
    # setup
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    stack.Push(node1)
    stack.Push(node2)
    stack.Push(node3)

    # execute
    result = stack.Pop()

    # assert
    assert result == node3
    assert stack.head == node2
    assert stack.size == 2


def test_delete_tail():
    # setup
    stack = StackLL()

    # execute
    result = stack.DeleteTail()

    # assert
    assert result is None
    assert stack.head is None
    assert stack.size == 0


def test_delete():
    # setup
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    stack.Push(node1)
    stack.Push(node2)
    stack.Push(node3)

    # execute
    result = stack.Delete(node1)

    # assert
    assert result is None
    assert stack.size == 3
    assert stack.head == node3
    assert stack.head.next == node2
    assert stack.head.next.next == node1


def test_sort():
    # setup
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    stack.Push(node4)
    stack.Push(node3)
    stack.Push(node2)
    stack.Push(node1)

    # execute
    stack.Sort()

    # assert
    assert stack.size == 4
    assert stack.head == node1
    assert stack.head.next == node2
    assert stack.head.next.next == node3
    assert stack.head.next.next.next == node4


def test_clear():
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    stack.Push(node1)
    stack.Push(node2)
    stack.Clear()
    assert stack.size == 0
    assert stack.head is None


def test_print(capsys):
    stack = StackLL()
    node1 = Node(1)
    node2 = Node(2)
    stack.Push(node1)
    stack.Push(node2)
    stack.Print()
    captured = capsys.readouterr()
    assert captured.out == "Stack size: 2\nContents of stack are...\n\n2\n1\n"
