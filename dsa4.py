from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while (True):
                if new_node.value == temp.value:
                    return False
                elif new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                elif new_node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_val(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
                    
        
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.contains(4))
print(my_tree.min_val(my_tree.root))
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
