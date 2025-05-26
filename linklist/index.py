
# initalise the linked list
class Node : 
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList : 

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def at_beginning(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # insert at end of the list 

    def at_end(self , data):
        new_node  = Node(data)

        if not self.head : 
            self.head  = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('None')


    # insert a specific index 
    def at_specific_index(self , index ,  data):
        if index < 0 :
            print('Index should be grater than 0')
        if index == 0 :
            self.at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0 
        while current and count < index -1 :
            current = current.next
            count += 1
        if not current:
            print('Index out of range')
        new_node.next = current.next
        current.next = new_node
    
    def delete_node(self ,index , data):
        if index < 0:
            print("Index must be non-negative")
        if not self.head:
            print("List is empty")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if not current.next:
            print("Index out of bounds")
        current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # Not found

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find_middle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    
    def reverse_linklist(self ):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def detect_cyle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    

            
ll = LinkedList()
ll.at_beginning(10)
ll.at_end(20)
ll.at_beginning(0)
ll.print_list()