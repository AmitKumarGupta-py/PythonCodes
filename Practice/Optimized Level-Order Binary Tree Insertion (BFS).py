from collections import deque
import graphviz

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_level_order(arr):
    if not arr:
        return None
    
    root = Node(arr[0])
    queue = deque([root])
    i = 1
    
    while i < len(arr):
        current = queue.popleft()
        
        if i < len(arr) and arr[i] is not None:
            current.left = Node(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            current.right = Node(arr[i])
            queue.append(current.right)
        i += 1
        
    return root

# Example usage
values = [1, 2, 3, 4, 5, 6, 7]  # Level-order input
root = insert_level_order(values)

# Inorder Traversal (to verify)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

print("Inorder Traversal:")
inorder_traversal(root)  # Output: 4 2 5 1 6 3 7

# 🌳 Tree Visualization
def visualize_tree(root):
    dot = graphviz.Digraph()

    def add_edges(node):
        if not node:
            return
        dot.node(str(node.value))
        if node.left:
            dot.edge(str(node.value), str(node.left.value))
            add_edges(node.left)
        if node.right:
            dot.edge(str(node.value), str(node.right.value))
            add_edges(node.right)
    
    add_edges(root)
    return dot

tree_graph = visualize_tree(root)
tree_graph.render("binary_tree", format="png", cleanup=False)  # Saves the tree as an image
tree_graph  # Displays the tree
