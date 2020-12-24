#!/usr/bin/env python3

class Node:
    
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    # Function to initialize Linked List
    def __init__(self):
        self.head = None

    # Print the list
    def traverse(self):
        if self.head == None:
            print("None")

        t = self.head
        while (t != None):
            if t.next != None:
                print(t.data, " -> ", end = " ")
            else:
                print(t.data, " -> None", end = " ")
            t = t.next
        print("")

    # Add to the end of the list
    def append(self, data):
        my_node = Node(data)
        if None == self.head:
            self.head = my_node
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = my_node

    # Add to the start of the list
    def add_to_start(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # Add data to the given position in the list
    def add_at_pos(self, pos, data):
        newNode = Node(data)
        if pos < 0:
            pos = 0

        if self.head == None:
            self.head = newNode
        else:
            dummy = Node(1)
            dummy.next = self.head
            t = dummy
            # Move ahead till you reach the last node or `pos` steps.
            while (t.next and pos > 0):
                t = t.next
                pos = pos - 1

            # Add new node
            newNode.next = t.next
            t.next = newNode

            # If new node is being inserted at the beginning, update head node
            if t == dummy:
                self.head = newNode

    # Delete last node of the list
    def delete_last(self):
        if self.head == None:
            return
        
        # If only one node in the list
        t = self.head
        if t.next == None:
            self.head = None
            t = None
            return
        
        while t.next.next != None:
            t = t.next
        t.next = None

    # Delete first element of the list
    def delete_first(self):
        if self.head == None:
            return
        
        self.head = self.head.next

    # Delete node with the specified value
    def delete_given_value(self, data):
        dummy = Node(1)
        dummy.next = self.head

        prev = dummy
        curr = self.head

        while (curr and curr.data != data):
            prev = curr
            curr = curr.next
        
        if (curr):
            prev.next = curr.next
            if (curr == self.head):
                self.head = self.head.next

    # Delete node at the given position
    def delete_from_pos(self, pos):
        if self.head == None:
            print("self.head == None!")
            return
        
        if pos < 0:
            pos = 0

        curr = self.head
        prev = None

        while (curr.next and pos > 0):
            prev = curr
            curr = curr.next
            pos = pos - 1
        
        if curr == self.head:
            self.head = curr.next
        else:
            prev.next = curr.next

    # Delete the full list
    def delete_list(self):
        while (self.head):
            self.head = self.head.next

    def length_list(self):
        len = 0
        curr = self.head

        while (curr):
            curr = curr.next
            len = len + 1
        
        return len
    
    def length_list_recursive(self):
        return self._length_list_recursive(self.head)
    
    def _length_list_recursive(self, head):
        if head == None:
            return 0
        if head.next == None:
            return 1
        
        return 1 + self._length_list_recursive(head.next)

class LinkedListTest:

    def __init__(self):
        self.head = None
    
    def test_append(self):
        print("test_append")
        my_list = LinkedList()

        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.traverse()

    def test_add_to_start(self):
        print("test_add_to_start")
        my_list = LinkedList()

        my_list.add_to_start(1)
        my_list.add_to_start(2)
        my_list.add_to_start(3)
        my_list.traverse()

    def test_add_at_pos(self):
        print("test_add_at_pos")
        my_list = LinkedList()
        my_list.add_at_pos(2, 1)
        my_list.add_at_pos(0, 2)
        my_list.add_at_pos(5, 3)
        my_list.add_at_pos(1, 4)
        my_list.traverse()

    def test_delete_last(self):
        print("test_delete_last")
        my_list = LinkedList()

        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.traverse()
        my_list.delete_last()
        my_list.traverse()

    def test_delete_first(self):
        print("test_delete_first")
        my_list = LinkedList()

        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.traverse()
        my_list.delete_first()
        my_list.traverse()
        my_list.delete_first()
        my_list.traverse()
        my_list.delete_first()
        my_list.traverse() # Print empty list

    def test_delete_given_value(self):
        print("test_delete_given_value")
        my_list = LinkedList()

        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.append(4)
        my_list.traverse()

        # Delete head node
        my_list.delete_given_value(1)
        my_list.traverse()

        # delete last node
        my_list.delete_given_value(4)
        my_list.traverse()

    def test_delete_from_pos(self):
        print("test_delete_from_pos")
        my_list = LinkedList()

        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.traverse()
        my_list.delete_from_pos(1)
        my_list.traverse()

    def test_delete_list(self):
        print("test_delete_list")
        my_list = LinkedList()

        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.traverse()
        my_list.delete_list()
        my_list.traverse()

    def test_length_list(self):
        print("test_length_list")
        my_list = LinkedList()
        my_list.add_to_start(1)
        my_list.add_to_start(2)
        my_list.add_to_start(3)
        len = my_list.length_list()
        print("len = ", len)

    def test_length_list_recursive(self):
        print("test_length_list_recursive")
        my_list = LinkedList()
        my_list.add_to_start(1)
        my_list.add_to_start(2)
        my_list.add_to_start(3)
        print("len = ", my_list.length_list_recursive())

    

def main():
    test_list = LinkedListTest()
    test_list.test_append()
    test_list.test_delete_last()
    test_list.test_add_to_start()
    test_list.test_add_at_pos()
    test_list.test_delete_first()
    test_list.test_delete_given_value()
    test_list.test_delete_from_pos()
    test_list.test_delete_list()
    test_list.test_length_list()
    test_list.test_length_list_recursive()

if __name__ == "__main__":
    main()
    