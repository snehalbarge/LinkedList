"""
Reverse a linked list using recursion and iteration and find the length of the linked list.
"""

import logging
logging.basicConfig(level=logging.INFO)

# Create node of the linked list
class LinkedListNode:
    # Initialize the Node for the Linked List
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a linked list
class LinkedList:
    # Initialize the first element/head for the Linked List
    def __init__(self):
        self.head = None


    # Recursive reverse linked list solution
    def reverseRecursive(self, curr, prev):
        """
        :param curr: Current Node
        :param prev: Previous Node
        :return: reversed linked list
        """

        if self.head is None:
            return
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseRecursive(next, curr)


    # Iterative reverse linked list solution
    def reverseIterative(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    # basically a stack data structure as a linked list
    def insert(self, new_data):
        """
        :param new_data: insert node in linked list

        """

        new_node = LinkedListNode(new_data)
        new_node.next = self.head
        self.head = new_node


    # checking the results by printing
    def printLinkedList(self):

        temp = self.head
        while (temp):

            logging.info(temp.data)
            temp = temp.next


    #find the length of linked list
    def length(self):
        """
        :return: returns length of the linked list

        """

        if self.head is None:
            return 0
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length


linked_list = LinkedList()
while True:
    try:
        x = int(input("Please enter a size of node : "))
        for i in range(x):
            number = int(input())
            linked_list.insert(number)
        break
    except ValueError:
        logging.error("Oops!That was no valid number.  Try again...")



print("length of linked list", linked_list.length())

print("Before reversing...")
linked_list.printLinkedList()


print("After reversing...")
linked_list.reverseIterative()

#linked_list.reverseRecursive(linked_list.head, None)

linked_list.printLinkedList()



# Code Covergae of linklist :

# Name          Stmts   Miss  Cover   Missing
# -------------------------------------------
# linklist.py      62     12    81%   12, 22-23, 29-30, 34, 39, 55, 58, 73, 77, 82, 86
#
