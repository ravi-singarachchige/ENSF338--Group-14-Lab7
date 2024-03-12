import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        return x

    def _lr_rotate(self, z):
        z.left = self._left_rotate(z.left)
        return self._right_rotate(z)

    def _rl_rotate(self, z):
        z.right = self._right_rotate(z.right)
        return self._left_rotate(z)

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        balance = self.get_balance(root)
        if balance > 1:
            if key < root.left.val:
                root = self._right_rotate(root)
                print("Case #3a: adding a node to an outside subtree")
            else:
                root = self._lr_rotate(root)
                print("Case #3b: adding a node to an inside subtree")
        elif balance < -1:
            if key > root.right.val:
                root = self._left_rotate(root)
                print("Case #3a: adding a node to an outside subtree")
            else:
                root = self._rl_rotate(root)
                print("Case #3b: adding a node to an inside subtree")
        else:
            print("Case #1: Pivot not detected")
        return root
    
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def get_balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


# Test cases
bst = BST()
bst.root = bst.insert(bst.root, 30)  # Case 1
bst.root = bst.insert(bst.root, 20)  # Case 1
bst.root = bst.insert(bst.root, 40)  # Case 2
bst.root = bst.insert(bst.root, 50)  # Case 2
bst.root = bst.insert(bst.root, 60)  # Case 3a
bst.root = bst.insert(bst.root, 10)  # Case 3b
bst.root = bst.insert(bst.root, 25)  # Case 3b
bst.root = bst.insert(bst.root, 35)  # Case 3b