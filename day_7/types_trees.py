# Types of Trees in Data Structures

#1. General Tree

# A node can have **any number of children**.

# ```text
#       A
#     / | \
#    B  C  D
#       |
#       E
# ```

# ---

# #### 2. Binary Tree

# Each node can have **at most 2 children** (left and right).

# ```text
#       1
#      / \
#     2   3
# ```

# ---

# #### 3. Full Binary Tree

# Every node has either **0 or 2 children**.

# ```text
#       1
#      / \
#     2   3
#    / \
#   4   5
# ```

# ---

# #### 4. Complete Binary Tree

# All levels are completely filled except possibly the last level, which is filled from left to right.

# ```text
#       1
#      / \
#     2   3
#    / \  /
#   4  5 6
# ```

# ---

# #### 5. Perfect Binary Tree

# All internal nodes have 2 children and all leaf nodes are at the same level.

# ```text
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
# ```

# ---

# #### 6. Balanced Binary Tree

# The height difference between left and right subtrees is small (usually ≤ 1).

# Examples:

# * AVL Tree
# * Red-Black Tree

# ---

# #### 7. Binary Search Tree (BST)

# For every node:

# * Left subtree values < Root
# * Right subtree values > Root

# ```text
#        8
#       / \
#      3   10
#     / \    \
#    1   6    14
# ```

# ---

# #### 8. AVL Tree

# A self-balancing BST where the height difference between left and right subtrees is at most 1.

# ---

# #### 9. Red-Black Tree

# A self-balancing BST that uses red and black colors to maintain balance.

# ---

# #### 10. Heap

# A complete binary tree.

# * **Max Heap**: Parent ≥ Children
# * **Min Heap**: Parent ≤ Children

# ```text
#       50
#      /  \
#    30    20
# ```

# ---

# ### types-

# 1. General Tree
# 2. Binary Tree
#  Full Binary Tree
#  Complete Binary Tree
#  Perfect Binary Tree
#  Balanced Binary Tree
# 3.Binary Search Tree (BST)
# 4. AVL Tree
# 5. Red-Black Tree