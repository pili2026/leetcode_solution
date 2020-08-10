class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, left, right):
        ans = 0
        stack = root

        while stack:
            node = stack.pop()
            print(node)
            if node:
                if left <= node.val <= right:
                    ans += node.val
                if left < node.val:
                    stack.append(node.left)
                if node.val < right:
                    stack.append(node.right)
        return ans

