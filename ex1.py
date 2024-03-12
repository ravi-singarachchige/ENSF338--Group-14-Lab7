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

def generate_tasks(n):
    tasks = []
    for _ in range(n):
        task = list(range(1, n+1))
        random.shuffle(task)
        tasks.append(task)
    return tasks

def measure_performance(bst, tasks):
    balance_values = []
    search_times = []
    for task in tasks:
        start_time = time.time()
        for item in task:
            bst.search(bst.root, item)
        end_time = time.time()
        search_times.append(end_time - start_time)
        balance_values.append(abs(bst.get_balance(bst.root)))
    return balance_values, search_times

def plot_performance(balance_values, search_times):
    plt.scatter(balance_values, search_times)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')
    plt.show()

bst = BST()
for i in range(1, 1001):
    bst.root = bst.insert(bst.root, i)

tasks = generate_tasks(1000)
balance_values, search_times = measure_performance(bst, tasks)
plot_performance(balance_values, search_times)