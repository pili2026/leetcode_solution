# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric_recursive(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = root.left
        right = root.right

        if left is None and right is None:
            return True
        return self.check(left, right)

    def check(self, node_1, node_2):
        if not node_1 and not node_2:
            return True
        if node_1 and not node_2:
            return False
        if not node_1 and node_2:
            return False
        if node_1.val != node_2.val:
            return False
        return self.check(node_1.left, node_2.right) and self.check(node_1.right, node_2.left)

    def is_symmetric_iteration(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([(root.left, root.right)])
        while queue:
            l, r = queue.popleft()
            if not l and not r:
                continue
            if l and r and l.val == r.val:
                queue.append((l.right, r.left))
                queue.append((l.left, r.right))
            else:
                return False
        return True


if __name__ == '__main__':
    binary_tree = Solution()
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(2)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)

    '''
    tree:
            1
        2       3
      4   5   6   7
    '''

    print(binary_tree.is_symmetric_recursive(node))
    print(binary_tree.is_symmetric_iteration(node))
