from __future__ import annotations


class TreeNode:
    def __init__(self, value, left: TreeNode = None, right: TreeNode = None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    node1 = TreeNode(25)
    node2 = TreeNode(75)

    root = TreeNode(50, node1, node2)
