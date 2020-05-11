# Calculate height of binary tree | Iterative & Recursive

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findTreeHeight(root):
    if root:
        return 1 + max(findTreeHeight(root.left), findTreeHeight(root.right))
    else:
        return 0


root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

print("The height of the binary tree is ", findTreeHeight(root))
