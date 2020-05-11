# Tree Traversals (Inorder, Preorder and Postorder)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is", preorder(root))

print("Inorder traversal of binary tree is", inorder(root))

print("Postorder traversal of binary tree is", postorder(root))
