class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Example usage:
my_linked_list = LinkedList()

print(my_linked_list.is_empty())
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)
my_linked_list.display()  # Output: 0 -> 1 -> 2 -> 3
print(my_linked_list.is_empty())

my_linked_list.delete(2)
my_linked_list.display()  # Output: 0 -> 1 -> 3