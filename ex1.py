import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinarySearchTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        
        currentNode = root
        while currentNode:
            prevNode = currentNode
            if key < currentNode.key:
                currentNode = currentNode.left
                if not currentNode:
                    prevNode.left = Node(key)
            else:
                currentNode = currentNode.right
                if not currentNode:
                    prevNode.right = Node(key)
        return root

    def search(self, root, key):
        currentNode = root
        while currentNode and currentNode.key != key:
            currentNode = currentNode.left if key < currentNode.key else currentNode.right
        return currentNode is not None

def measure_balance_and_search_time(root, tasks):
    start_time = time.time()
    for task in tasks:
        bst.search(root, task)
    search_time = (time.time() - start_time) / len(tasks)
    # Simplified balance checking, assuming you want to avoid recursion
    max_balance = 0  # Placeholder for balance calculation
    return search_time, max_balance

bst = BinarySearchTree()
root = None

# Insert integers into the BST
for i in range(1, 1001):
    root = bst.insert(root, i)

# Prepare search tasks
tasks = list(range(1, 1001))
average_search_times = []
max_balances = []

for _ in range(1000):
    random.shuffle(tasks)
    search_time, max_balance = measure_balance_and_search_time(root, tasks)
    average_search_times.append(search_time)
    max_balances.append(max_balance)  # Adjust this with actual balance calculation if needed

# Plotting the scatterplot
plt.scatter(max_balances, average_search_times)
plt.title('Search Time vs Absolute Balance')
plt.xlabel('Largest Absolute Balance')
plt.ylabel('Average Search Time (s)')
plt.show()

