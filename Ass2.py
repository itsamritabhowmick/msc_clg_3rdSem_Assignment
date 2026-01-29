#Write a Python Program to find Wining path from a given game tree using Adversarial Search(Min-Max Search). 

# Define the Node structure
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children else []

# Min-Max function
def minimax(node, depth, is_maximizing):
    # If leaf node
    if not node.children:
        return node.value

    if is_maximizing:
        best_value = float('-inf')
        for child in node.children:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node.children:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value
# Leaf nodes
leaf1 = Node(3)
leaf2 = Node(12)
leaf3 = Node(8)
leaf4 = Node(2)
leaf5 = Node(4)
leaf6 = Node(6)
leaf7 = Node(14)
leaf8 = Node(5)

# Level 2 nodes
node4 = Node(2, [leaf1, leaf2])
node5 = Node(6, [leaf3, leaf4])
node6 = Node(9, [leaf5, leaf6])
node7 = Node(7, [leaf7, leaf8])

# Level 1 nodes
node2 = Node(5, [node4, node5])
node3 = Node(3, [node6, node7])

# Root node
root = Node(4, [node2, node3])

# Run Min-Max
result = minimax(root, 3, True)

print("The optimal value using Min-Max is:", result)
