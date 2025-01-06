class AVLNode:
    def __init__(self, order_id, order_detail):
        self.order_id = order_id
        self.order_detail = order_detail
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, order_id, order_detail):
        if not node:
            return AVLNode(order_id, order_detail)
        if order_id < node.order_id:
            node.left = self.insert(node.left, order_id, order_detail)
        elif order_id > node.order_id:
            node.right = self.insert(node.right, order_id, order_detail)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and order_id < node.left.order_id:
            return self.rotate_right(node)

        if balance < -1 and order_id > node.right.order_id:
            return self.rotate_left(node)

        if balance > 1 and order_id > node.left.order_id:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and order_id < node.right.order_id:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f"Order ID: {node.order_id}, Details: {node.order_detail}")
            self.inorder_traversal(node.right)

    def insert_order(self, order_id, order_detail):
        self.root = self.insert(self.root, order_id, order_detail)
        print(f"Order '{order_detail}' with ID {order_id} added successfully!")

    def display_orders(self):
        print("Orders in AVL Tree (sorted by Order ID):")
        self.inorder_traversal(self.root)
        print("----------------")


avl_tree = AVLTree()
avl_tree.insert_order(101, "Order for Python Programming")
avl_tree.insert_order(203, "Order for Data Science Essentials")
avl_tree.insert_order(150, "Order for Web Development with Django")
avl_tree.insert_order(120, "Order for Machine Learning Basics")
avl_tree.insert_order(180, "Order for Cybersecurity Fundamentals")
print()
avl_tree.display_orders()
