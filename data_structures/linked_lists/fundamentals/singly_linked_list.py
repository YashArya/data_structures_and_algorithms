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
        t = self.head
        while (t != None):
            print(t.data, " -> ", end = " ")
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
    
    # Delete last node of the list
    def delete(self):
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


def main():
    my_list = LinkedList()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.traverse()
    my_list.delete()
    my_list.traverse()

if __name__ == "__main__":
    main()
    