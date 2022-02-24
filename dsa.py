class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head.next
            temp.prev = None
            self.head.next = None
            self.head = temp
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next
            before.next = new_node
            new_node.prev = before
            new_node.next = after
            after.prev = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.get(index)
            before = temp.prev
            after = temp.next
            before.next = after
            after.prev = before
            self.length -= 1
            return True
            
my_ll = DLL(7)

my_ll.append(60)
my_ll.prepend(5)
my_ll.insert(1, 69)
my_ll.remove(1)
my_ll.print_list()

