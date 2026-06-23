# creating a tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 1. Create root node
root = TreeNode(1)

# 2. Insert / create child nodes
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# 3. Connect nodes
root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

# Tree:
#        1
#       / \
#      2   3
#     / \
#    4   5


# 4. Access nodes
print("Root:", root.val)
print("Left child of root:", root.left.val)
print("Right child of root:", root.right.val)
print("Left child of node 2:", root.left.left.val)


# 5. Print tree using preorder traversal
# def print_tree(root):
#     if root is None:
#         return

#     print(root.val, end=" ")
#     print_tree(root.left)
#     print_tree(root.right)


# print("Tree:")
# print_tree(root)

# Print tree structure
print("      ", root.val)
print("     / \\")
print("   ", root.left.val, " ", root.right.val)
print("   / \\")
print(root.left.left.val, " ", root.left.right.val)

#  deletion


 
# traversal(DFS,BFS)--

# BFS-
# Time Complexity: O(n)
# Space Complexity: O(n)

# DFS-
# Time Complexity: O(n)
# Space Complexity: O(h), where h = height of tree


# | BFS                                        | DFS                           |
# | ------------------------------------------ | ----------------------------- |
# | Level by level                             | Depth by depth                |
# | Uses Queue                                 | Uses Stack/Recursion          |
# | Level Order Traversal                      | Preorder, Inorder, Postorder  |
# | More memory on wide trees                  | Less memory on balanced trees |
# | Good for shortest path in unweighted graph | Good for deep exploration     |
