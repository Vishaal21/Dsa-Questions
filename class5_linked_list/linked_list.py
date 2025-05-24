class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LL:

    def __init__(self):
        self.head = None
     

    def insert_at_start(self, data):

        node = Node(data)
        node.next = self.head
        self.head = node

        return

    def insert_at_end(self, data):

        node = Node(data)
        current = self.head

        if current == None:
            self.head = node
        else:
            while current.next != None:
                current = current.next

            # now current is pointing to last node
            current.next = node
            node.next = None

    def insert_after(self, insert_after_this_data, data_to_be_inserted):
        node = Node(data_to_be_inserted)

        current = self.head
        
        while current.data != insert_after_this_data:
            current = current.next
            if current == None:
                print(f"can not insert after {insert_after_this_data} this data as it does not exists")
                return
            
        node.next = current.next
        current.next = node


    def display(self):

        current = self.head

        if current is None:
            print("linked list is empty")
            return
        


        while current:
            print(current.data)
            current = current.next
      

    def delete_first(self):

        if self.head == None:
            return
        
        self.head = self.head.next

    def delete_last(self):

        if self.head == None:
            return
        
        current = self.head
        
        while current.next.next != None:
            current = current.next

        current.next = None
            

linked_list = LL()

# linked_list.insert_at_start(1)
# linked_list.insert_at_start(2)


linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(5)

linked_list.insert_after(3, 4)
# linked_list.delete_first()
linked_list.delete_last()


linked_list.display()


# linked_list.insert_after(3, 4)
# linked_list.delete_last()
# linked_list.display()


# linked_list.is_element_exists(7)
