# Definition for singly-linked list.
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class contains a Node object
class LinkedList:
# Function to initialize head
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
 
if __name__=='__main__':        
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printList()
