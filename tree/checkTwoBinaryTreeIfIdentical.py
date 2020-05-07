# Check if two binary trees are identical or not | Iterative & Recursive
# Write an efficient algorithm to check if two binary trees are identical or
# not. i.e. if they have identical structure & their contents are also same

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getData(self):
        return self.value


def checkTwoBinaryTreeIfIdentical(root1, root2):
    if not root1 and not root2:
        return True
    elif (root1 and root2) and (root1.value == root2.value):
        return checkTwoBinaryTreeIfIdentical(root1.left, root2.left) \
               and checkTwoBinaryTreeIfIdentical(root1.right, root2.right)


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.left.right.left = Node(8)
root1.left.right.left.left = Node(9)
root1.left.right.left.left.left = Node(10)
root1.right.right = Node(7)
root1.right.right.right = Node(11)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.left.right.left = Node(8)
root2.left.right.left.left = Node(9)
root2.left.right.left.left.left = Node(10)
root2.right.right = Node(7)
root2.right.right.right = Node(11)

print("root1 and root2 are Identical " if checkTwoBinaryTreeIfIdentical(root1, root2)
      else "root1 and root2 are not Identical ")

root1.right.right.right = Node(12)
print("root1 and root2 are Identical " if checkTwoBinaryTreeIfIdentical(root1, root2)
      else "root1 and root2 are not Identical ")
