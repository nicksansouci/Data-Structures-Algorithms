from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        if self.length == 0:
            return None
        else:
            while self.head is not None:
                print(self.head.value)
                self.head = self.head.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            pre.next = None
            self.tail = pre
            self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            self.length -= 1

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = self.head
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
my_list = LinkedList(20)

my_list.append(21)
my_list.append(22)
my_list.prepend(1)
my_list.insert(1, 3)
my_list.remove(2)
my_list.print_list()