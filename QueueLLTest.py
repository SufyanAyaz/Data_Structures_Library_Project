import pytest
from myLib.datastructures.Linear.QueueLL import QueueLL
from myLib.datastructures.nodes.SNode import Node


def test_init_default():
    queue = QueueLL()
    assert queue.head is None
    assert queue.tail is None
    assert queue.size == 0


def test_init_with_head():
    node = Node(1)
    queue = QueueLL(head=node)
    assert queue.head == node
    assert queue.tail == node
    assert queue.size == 1


def test_enqueue():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)

    # execute
    queue.Enqueue(node1)
    queue.Enqueue(node2)

    # assert
    assert queue.size == 2
    assert queue.head == node1
    assert queue.tail == node2
    assert queue.head.next == node2
    assert queue.tail.next is None


def test_InsertHead():
    # setup
    queue = QueueLL()
    node = Node(1)

    # execute
    queue.Enqueue(node)

    # assert
    assert queue.head == node
    assert queue.tail == node
    assert queue.size == 1


def test_Insert():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    queue.Enqueue(node1)
    queue.Enqueue(node3)

    # execute
    temp = queue.Dequeue()
    queue.Enqueue(node2)
    queue.Enqueue(temp)

    # assert
    assert queue.Dequeue() == node3
    assert queue.Dequeue() == node2
    assert queue.Dequeue() == node1
    assert queue.size == 0


def test_SortedInsert():
    # setup
    queue = QueueLL()

    # execute
    node1 = Node(1)
    queue.SortedInsert(node1)
    node2 = Node(2)
    queue.SortedInsert(node2)
    node3 = Node(3)
    queue.SortedInsert(node3)
    node4 = Node(4)
    queue.SortedInsert(node4)

    # assert
    if queue.size > 0:
        assert queue.head == node4
        assert queue.head.next.data == 3
        assert queue.head.next.next.data == 2
        assert queue.head.next.next.next.data == 1
    else:
        assert queue.head is None


def test_dequeue():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    queue.Enqueue(node1)
    queue.Enqueue(node2)

    # execute
    dequeued_node = queue.Dequeue()

    # assert
    assert dequeued_node == node1
    assert queue.size == 1
    assert queue.head == node2
    assert queue.tail == node2
    assert queue.head.next is None
    assert queue.tail.next is None


def test_dequeue_empty():
    # setup
    queue = QueueLL()

    # execute
    dequeued_node = queue.Dequeue()

    # assert
    assert dequeued_node is None
    assert queue.size == 0
    assert queue.head is None
    assert queue.tail is None


def test_search():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    queue.Enqueue(node1)
    queue.Enqueue(node2)

    # execute
    found_position = queue.Search(node2)
    not_found_position = queue.Search(Node(3))

    # assert
    assert found_position == 2
    assert not_found_position is None


def test_delete_tail():
    # setup
    queue = QueueLL()

    # execute
    result = queue.DeleteTail()

    # assert
    assert result is None
    assert queue.head is None
    assert queue.size == 0


def test_delete():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    queue.Enqueue(node1)
    queue.Enqueue(node2)
    queue.Enqueue(node3)

    # execute
    result = queue.Delete(node1)

    # assert
    assert result is None
    assert queue.size == 3
    assert queue.head == node1
    assert queue.head.next == node2
    assert queue.head.next.next == node3


def test_sort():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    queue.Enqueue(node4)
    queue.Enqueue(node3)
    queue.Enqueue(node2)
    queue.Enqueue(node1)

    # execute
    queue.Sort()

    # assert
    assert queue.size == 4
    assert queue.head == node4
    assert queue.head.next == node3
    assert queue.head.next.next == node2
    assert queue.head.next.next.next == node1


def test_clear():
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    queue.Enqueue(node1)
    queue.Enqueue(node2)

    # execute
    queue.Clear()

    # assert
    assert queue.size == 0
    assert queue.head is None
    assert queue.tail is None


def test_print(capsys):
    # setup
    queue = QueueLL()
    node1 = Node(1)
    node2 = Node(2)
    queue.Enqueue(node1)
    queue.Enqueue(node2)

    # execute
    queue.Print()

    # assert
    captured = capsys.readouterr()
    assert "Queue size: 2\n" in captured.out
    assert "Contents of queue are...\n" in captured.out
    assert "1\n" in captured.out
    assert "2\n" in captured.out
