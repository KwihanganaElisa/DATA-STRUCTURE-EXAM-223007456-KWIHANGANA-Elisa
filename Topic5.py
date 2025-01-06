# Binary Tree implementation for dynamically tracking data

class BinaryTreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key, data):
        if not node:
            return BinaryTreeNode(key, data)
        if key < node.key:
            node.left = self.insert(node.left, key, data)
        else:
            node.right = self.insert(node.right, key, data)
        return node

    def insert_data(self, key, data):
        self.root = self.insert(self.root, key, data)
        print(f"Data with key '{key}' added successfully!")

    def search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def search_data(self, key):
        result = self.search(self.root, key)
        if result:
            print(f"Data found: Key: {result.key}, Data: {result.data}")
        else:
            print(f"No data found for key '{key}'.")

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f"Key: {node.key}, Data: {node.data}")
            self.inorder_traversal(node.right)

    def display_data(self):
        print("Tracked Data (sorted by keys):")
        self.inorder_traversal(self.root)
        print("----------------")



binary_tree = BinaryTree()

binary_tree.insert_data(101, "User enrolled in Python Programming")
binary_tree.insert_data(203, "User enrolled in Data Science Essentials")
binary_tree.insert_data(150, "User enrolled in Web Development with Django")
binary_tree.insert_data(120, "User completed Machine Learning Basics")
binary_tree.insert_data(180, "User enrolled in Cybersecurity Fundamentals")

binary_tree.display_data()

binary_tree.search_data(150)
binary_tree.search_data(999)
