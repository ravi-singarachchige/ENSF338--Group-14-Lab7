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
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case 3 not supported")
        elif balance < -1:
            if key > root.right.val:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case 3 not supported")
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
bst.root = bst.insert(bst.root, 10)  # Case 1
bst.root = bst.insert(bst.root, 20)  # Case 1
bst.root = bst.insert(bst.root, 30)  # Case 2
bst.root = bst.insert(bst.root, 40)  # Case 2
bst.root = bst.insert(bst.root, 25)  # Case 3