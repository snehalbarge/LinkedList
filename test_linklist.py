"""
unit test cases for the linked list
"""
import unittest
from linklist import LinkedList


class TestLinkedList(unittest.TestCase):

    LIST_SIZE = 7
    BIG_LIST_SIZE = 1000000


    def test_list_iterative(self):

        filled_linked_list = self.create_list(TestLinkedList.LIST_SIZE)
        filled_linked_list.reverseIterative()

        self.assertEqual(filled_linked_list.length(), TestLinkedList.LIST_SIZE)
        self.assertIsNotNone(filled_linked_list.head, None)
        current = filled_linked_list.head
        counter = 7
        while current is not None:
            self.assertEqual(current.data, counter)
            current = current.next
            counter -= 1


    def test_list_recursive(self):

        filled_linked_list = self.create_list(TestLinkedList.LIST_SIZE)
        filled_linked_list.reverseRecursive(filled_linked_list.head, None)

        self.assertEqual(filled_linked_list.length(), TestLinkedList.LIST_SIZE)
        self.assertIsNotNone(filled_linked_list.head, None)
        current = filled_linked_list.head
        counter = 7
        while current is not None:
            self.assertEqual(current.data, counter)
            current = current.next
            counter -= 1


    def test_empty_list_iterative(self):
        empty_linked_list = LinkedList()
        empty_linked_list.reverseIterative()
        self.assertEqual(empty_linked_list.head, None)


    def test_giant_list_iterative(self):
        big_list = self.create_list(TestLinkedList.BIG_LIST_SIZE)
        big_list.reverseIterative()
        self.assertEqual(big_list.length(), TestLinkedList.BIG_LIST_SIZE)


    def test_giant_list_recursive(self):
        big_list = self.create_list(TestLinkedList.BIG_LIST_SIZE)
        self.assertRaises(RuntimeError, big_list.reverse_recursive)


    def create_list(self, length):
        alist = LinkedList()
        for i in range(length, 0, -1):
            alist.insert(i)
        return alist






