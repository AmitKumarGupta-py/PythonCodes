class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # If subtree is unbalanced, propagate -1
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return height(root) != -1

# Constructing the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)
root.right.right.right = Node(7)

print(is_balanced(root))  # Output: False (since right subtree is deeper)
